from rest_framework import views
from rest_framework.response import Response

# Create your views here.
class HelloWorldView(views.APIView):
    def get(self, request):
        message = {'message': 'Hello, World!'}
        return Response(message)