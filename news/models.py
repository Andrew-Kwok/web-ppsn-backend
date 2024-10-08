from django.db import models
from djrichtextfield.models import RichTextField

class Author(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

class News(models.Model):
    headline = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='news-images/')
    content = RichTextField()

    # Publication Date & Last Updateed date
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    authors = models.ManyToManyField(Author)
    