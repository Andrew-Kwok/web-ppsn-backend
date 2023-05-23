from rest_framework import serializers
from .models import Question

class QuestionSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField()
    email = serializers.EmailField()
    question_text = serializers.CharField()

    class Meta:
        model = Question
        fields = '__all__'