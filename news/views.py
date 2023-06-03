from rest_framework.response import Response
from rest_framework import views

from .models import News
from .serializers import NewsSerializer

# Create your views here.
class NewsView(views.APIView):
    def get(self, request, id: int = None):
        if id is not None:
            news = News.objects.get(id=id)
            serializer = NewsSerializer(news)
        else:
            news = News.objects.all()
            serializer = NewsSerializer(news, many=True)
        
        return Response(serializer.data)
        