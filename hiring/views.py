from rest_framework.response import Response
from rest_framework import views, status

from .serializer import RegistrationFormFileSerializer

import io
import docx
import xml.etree.ElementTree as ET

def convert_docx_to_model(docx_file):
    doc = docx.Document(docx_file)

    xml_content = doc.part._element.xml
    xml_file = io.StringIO(xml_content)

    tree = ET.parse(xml_file)
    root = tree.getroot()

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

            # Write the tag and data to the CSV file
            print(tag, plain_text)


# Create your views here.
class RegistrationFormUploadView(views.APIView):
    def post(self, request, format=None):
        serializer = RegistrationFormFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
    
            docx_file = request.FILES['registration_form']
            convert_docx_to_model(docx_file)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
