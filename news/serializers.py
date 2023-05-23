from rest_framework import serializers
from .models import Author, News

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['full_name']

class NewsSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    
    class Meta:
        model = News
        fields = ['headline', 'picture', 'content', 'pub_date', 'upd_date', 'authors']
