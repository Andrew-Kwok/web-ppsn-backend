from django.contrib import admin

from .models import Author, News

class AuthorAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )
    list_display = ['full_name']

class NewsAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'pub_date', 'upd_date',)
    list_display = ['pub_date', 'upd_date', 'headline']
    ordering = ['-pub_date']


admin.site.register(Author, AuthorAdmin)
admin.site.register(News, NewsAdmin)