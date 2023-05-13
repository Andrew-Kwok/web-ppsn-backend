from django.contrib import admin

from .models import Question
class QuestionAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'id', )
    list_display = ['created_at', 'full_name', 'email']
    ordering = ['-created_at']

admin.site.register(Question, QuestionAdmin)