from django.contrib import admin

from .models import Author, News

class AuthorAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )
    list_display = ['full_name']

class NewsAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_at', 'updated_at',)
    list_display = ['created_at', 'updated_at', 'headline']
    ordering = ['-created_at']


admin.site.register(Author, AuthorAdmin)
admin.site.register(News, NewsAdmin)