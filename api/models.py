from django.db import models

# Create your models here.
class Question(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    question_text = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Question from {self.full_name}({self.email})'
    