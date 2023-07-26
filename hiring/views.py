import io
import os
import json
import tempfile
import datetime
import xml.etree.ElementTree as ET

from typing import Dict

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials

import docx

from .constants import (
    REGISTRATION_FORM_EMPTY_VALUE,
    REGISTRATION_FORM_DATE_FIELD,
    REGISTRATION_FORM_BOOLEAN_FIELD,
    REGISTRATION_FORM_DATA_MAPPING,
    REGISTRATION_FORM_ORGANIZATION_MAPPING,
    REGISTRATION_FORM_ACHIEVEMENT_MAPPING,
    REGISTRATION_FORM_EXPERIENCE_MAPPING,
    REGISTRATION_FORM_SCHOLARSHIP_MAPPING,
    REGISTRATION_FORM_PUBLICATION_MAPPING,
    REGISTRATION_FORM_LANGUAGE_MAPPING,
    REGISTRATION_FORM_SKILL_MAPPING,
    REGISTRATION_FORM_CHOICE_MAPPING,
)
from . import models
from .serializers import RegistrationFormFileSerializer



def convertDate(date_string, format):
    date = datetime.datetime.strptime(date_string, format)
    formatted_date = date.strftime("%Y-%m-%d")
    return formatted_date


class SaveDocxToDatabaseError(Exception):
    pass


def saveDocxToDatabase(docx_file, gdrive_link) -> None:
    # convert .docx to .xml 
    doc = docx.Document(docx_file)
    xml_content = doc.part._element.xml
    xml_file = io.StringIO(xml_content)

    # extract registrant data
    tree = ET.parse(xml_file)
    root = tree.getroot()
    registrant_data = [] 
    email_value, dob_value = None, None

    for control in root.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}sdt'):        
        # Find the tag of the content control
        tag_node = control.find(
            './{http://schemas.openxmlformats.org/wordprocessingml/2006/main}sdtPr/'
            '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tag'
        )
        if tag_node is not None:
            tag = tag_node.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val')

            # Find the plain text content of the content control
            plain_text = ''
            for t in control.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'):
                if t.text:
                    plain_text += t.text

            # if plain_text not in REGISTRATION_FORM_EMPTY_VALUE:
            if plain_text not in REGISTRATION_FORM_EMPTY_VALUE:
                if tag == 'email':
                    email_value = plain_text.strip()
                elif tag == 'tanggal_lahir':
                    dob_value = plain_text.strip()
                else:
                    registrant_data.append((tag.strip(), plain_text.strip()))

    if email_value is None:
        raise SaveDocxToDatabaseError('email: missing or unreadable')
    try:
        validate_email(email_value)
    except ValidationError:
        raise SaveDocxToDatabaseError('email: invalid format')

    if dob_value is None:
        raise SaveDocxToDatabaseError('date of birth: missing or unreadable')
    try:
        dob_value = convertDate(dob_value, "%A, %d %B %Y")
    except ValueError:
        raise SaveDocxToDatabaseError('date of birth: invalid format')

    # storing the data
    error_notes = []
    reg_data = models.RegistrationData.objects.create(email=email_value, tanggal_lahir=dob_value, tautan_dokumen_drive_ppsn=gdrive_link)
    reg_data_skill = models.RegistrationDataSkill.objects.create(registration_data=reg_data)
    reg_data_committee = models.RegistrationDataCommitteeDecision.objects.create(registration_data=reg_data)
    reg_data_organization: Dict[str, models.RegistrationDataOrganization] = dict()
    reg_data_achievement: Dict[str, models.RegistrationDataAchievement] = dict()
    reg_data_scholarship: Dict[str, models.RegistrationDataScholarship] = dict()
    reg_data_experience: Dict[str, models.RegistrationDataExperience] = dict()
    reg_data_publication: Dict[str, models.RegistrationDataPublication] = dict()
    reg_data_language: Dict[str, models.RegistrationDataLanguage] = dict()
    reg_data_division_choice: Dict[str, models.RegistrationDataDivisionChoice] = dict()

    for (key, value) in registrant_data:
        if key in REGISTRATION_FORM_BOOLEAN_FIELD:
            value = value.upper() == REGISTRATION_FORM_BOOLEAN_FIELD[key]

        try:
            if key in REGISTRATION_FORM_DATA_MAPPING:
                if key in REGISTRATION_FORM_DATE_FIELD:
                    value = convertDate(value, REGISTRATION_FORM_DATE_FIELD[key])
                setattr(reg_data, REGISTRATION_FORM_DATA_MAPPING[key], value)
        
            elif key in REGISTRATION_FORM_SKILL_MAPPING:
                setattr(reg_data_skill, REGISTRATION_FORM_SKILL_MAPPING[key], value)
            
            elif key in REGISTRATION_FORM_ORGANIZATION_MAPPING:
                field, idx = REGISTRATION_FORM_ORGANIZATION_MAPPING[key]
                if field in REGISTRATION_FORM_DATE_FIELD:
                    value = convertDate(value, REGISTRATION_FORM_DATE_FIELD[field])
                if idx not in reg_data_organization:
                    reg_data_organization[idx] = models.RegistrationDataOrganization.objects.create(registration_data=reg_data)
                setattr(reg_data_organization[idx], field, value)
                
            elif key in REGISTRATION_FORM_ACHIEVEMENT_MAPPING:
                field, idx = REGISTRATION_FORM_ACHIEVEMENT_MAPPING[key]
                if idx not in reg_data_achievement:
                    reg_data_achievement[idx] = models.RegistrationDataAchievement.objects.create(registration_data=reg_data)
                setattr(reg_data_achievement[idx], field, value)

            elif key in REGISTRATION_FORM_EXPERIENCE_MAPPING:
                field, idx = REGISTRATION_FORM_EXPERIENCE_MAPPING[key]
                if field in REGISTRATION_FORM_DATE_FIELD:
                    value = convertDate(value, REGISTRATION_FORM_DATE_FIELD[field])
                if idx not in reg_data_experience:
                    reg_data_experience[idx] = models.RegistrationDataExperience.objects.create(registration_data=reg_data)
                setattr(reg_data_experience[idx], field, value)

            elif key in REGISTRATION_FORM_SCHOLARSHIP_MAPPING:
                field, idx = REGISTRATION_FORM_SCHOLARSHIP_MAPPING[key]
                if idx not in reg_data_scholarship:
                    reg_data_scholarship[idx] = models.RegistrationDataScholarship.objects.create(registration_data=reg_data)
                setattr(reg_data_scholarship[idx], field, value)

            elif key in REGISTRATION_FORM_PUBLICATION_MAPPING:
                field, idx = REGISTRATION_FORM_PUBLICATION_MAPPING[key]
                if idx not in reg_data_publication:
                    reg_data_publication[idx] = models.RegistrationDataPublication.objects.create(registration_data=reg_data)
                setattr(reg_data_publication[idx], field, value)

            elif key in REGISTRATION_FORM_LANGUAGE_MAPPING:
                field, idx = REGISTRATION_FORM_LANGUAGE_MAPPING[key]
                if idx not in reg_data_language:
                    reg_data_language[idx] = models.RegistrationDataLanguage.objects.create(registration_data=reg_data)
                setattr(reg_data_language[idx], field, value)
            
            elif key in REGISTRATION_FORM_CHOICE_MAPPING:
                field, idx = REGISTRATION_FORM_CHOICE_MAPPING[key]
                if idx not in reg_data_division_choice:
                    reg_data_division_choice[idx] = models.RegistrationDataDivisionChoice.objects.create(registration_data=reg_data)
                setattr(reg_data_division_choice[idx], field, value)
        except Exception as e:
            error_notes.append(str(e))

    reg_data.error_notes = ';\n'.join(error_notes)

    # remove old data
    old_data = models.RegistrationData.objects.filter(email=email_value, tanggal_lahir=dob_value)
    old_data.delete()

    # saving to database
    reg_data.save()
    reg_data_skill.save()
    reg_data_committee.save()

    for _model in reg_data_organization.values():
        _model.save()
    for _model in reg_data_achievement.values():
        _model.save()
    for _model in reg_data_scholarship.values():
        _model.save()
    for _model in reg_data_experience.values():
        _model.save()
    for _model in reg_data_publication.values():
        _model.save()
    for _model in reg_data_language.values():
        _model.save()
    for _model in reg_data_division_choice.values():
        _model.save()


class UploadFormToDriveException(Exception):
    pass


def uploadFormToDrive(docx_file):
    CREDENTIALS_FILE = os.path.join(os.path.dirname(__file__), 'gcloud_key', 'credentials.json')
    TOKEN_FILE = os.path.join(os.path.dirname(__file__), 'gcloud_key', 'token.json')
    GDRIVE_FOLDER = '1mLm935x548vuwNR2UxTSK6QkGdirm28M'
    SCOPES = ['https://www.googleapis.com/auth/drive']

    if not os.path.exists(CREDENTIALS_FILE):
        raise UploadFormToDriveException("error uploading to drive: credentials not found")

    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())

    try:
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(docx_file.read())
            temp_file_path = temp_file.name

        service = build('drive', 'v3', credentials=creds)


        # Upload the file to Google Drive
        media = MediaFileUpload(temp_file_path, mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        request = service.files().create(
            media_body=media,
            body={'name': docx_file.name, 'parents': [GDRIVE_FOLDER]}
        )
        response = request.execute()

    except HttpError as error:
        raise UploadFormToDriveException(f'An error occurred: {error}')

    file_id = response['id']
    link = f"https://drive.google.com/file/d/{file_id}"

    return link


# Create your views here.
class RegistrationFormUploadView(APIView):
    def post(self, request, format=None):
        serializer = RegistrationFormFileSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()
    
            docx_file = request.FILES['registration_form']

            try:
                link = uploadFormToDrive(docx_file)
            except UploadFormToDriveException:
                return Response({'message': 'file upload to drive failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            try:
                saveDocxToDatabase(docx_file, link)
            except SaveDocxToDatabaseError as e:
                return Response({'message': str(e)})

            response = {'message': 'file successfully saved'}
            return Response(response, status=status.HTTP_200_OK)

        response = {'message': serializer.errors}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class RegistrationFormGetUUID(APIView):    
    def post(self, request, format=None):
        try:
            json_data = json.loads(request.body)
        except json.JSONDecodeError:
            response = {'error': 'Invalid JSON Data'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        email = json_data['email']
        if email is None:
            response = {'error': 'missing email'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        tanggal_lahir = json_data['tanggal_lahir']
        if tanggal_lahir is None:
            response = {'error': 'missing tanggal lahir'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        try:
            tanggal_lahir = datetime.datetime.strptime(tanggal_lahir, "%Y-%m-%d")
        except ValueError as e:
            response = {'error': 'wrong tanggal_lahir format'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        registration_data = models.RegistrationData.objects.filter(email=email, tanggal_lahir=tanggal_lahir)
        if len(registration_data) == 0:
            response = {'error': f'form with email {email} and tanggal lahir {tanggal_lahir} not found'}
            return Response(response, status=status.HTTP_404_NOT_FOUND)
        elif len(registration_data) >= 2:
            response = {'error': f'multiple forms found. Please contact an admin'}
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        response = {'uuid': registration_data[0].id}
        return Response(response, status=status.HTTP_200_OK)


class RegistrationFormGetDecision(APIView):
    def get(self, request, id):
        registration_data = models.RegistrationData.objects.get(id=id)
        if registration_data is None:
            return Response({"error": "Registration data not found."}, status=status.HTTP_404_NOT_FOUND)

        decision = registration_data.hasil_seleksi.status_lulus
        if decision is None:
            return Response({"error": "Registration data not graded. Contact an admin."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        response = {
            "nama": registration_data.nama_lengkap,
            "email": registration_data.email,
            "tanggal_lahir": registration_data.tanggal_lahir.strftime("%A, %d %B %Y"),
            "status": decision
        }

        return Response(response, status=status.HTTP_200_OK)
