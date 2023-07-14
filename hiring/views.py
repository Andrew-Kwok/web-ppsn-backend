import io
import os
import tempfile
import datetime
import xml.etree.ElementTree as ET

from typing import Dict

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

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


def saveDocxToDatabase(docx_file, gdrive_link) -> None:
    # convert .docx to .xml 
    doc = docx.Document(docx_file)
    xml_content = doc.part._element.xml
    xml_file = io.StringIO(xml_content)

    # extract registrant data
    tree = ET.parse(xml_file)
    root = tree.getroot()
    registrant_data = [] 
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
                registrant_data.append((tag, plain_text))
            

    # storing the data
    error_notes = []
    reg_data = models.RegistrationData.objects.create(tautan_dokumen_drive_ppsn=gdrive_link)
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
        value = value.strip()
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

    reg_data.error_notes = ';'.join(error_notes)

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
    GDRIVE_FOLDER = os.getenv('GDRIVE_PARENT_FOLDER_ID')
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
            
            saveDocxToDatabase(docx_file, link)

            response = {'message': 'file successfully saved'}
            return Response(response, status=status.HTTP_200_OK)

        response = {'message': serializer.errors}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
