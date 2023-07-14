from rest_framework import serializers
from .models import RegistrationFormFile

class RegistrationFormFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationFormFile
        fields = ('registration_form',)
