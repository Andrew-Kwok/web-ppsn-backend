from rest_framework import serializers
from .models import Author, News

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['full_name']

class NewsSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S.%f')
    updated_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S.%f')

    class Meta:
        model = News
        fields = ['id', 'headline', 'picture', 'content', 'created_at', 'updated_at', 'authors']
