from rest_framework import views, status
from rest_framework.response import Response

from .models import Question
from .serializers import QuestionSerializer

from django.core import serializers

import json


# Create your views here.
class HelloWorldView(views.APIView):
    def get(self, request):
        message = {'message': 'Hello, World!'}
        return Response(message)


class QuestionView(views.APIView):
    def get(self, request):
        questions = Question.objects.all()
        json_data = serializers.serialize('json', questions)
        return Response(json.loads(json_data), status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
        # print(request.data)
        # serializer = QuestionSerializer(data=request.data)