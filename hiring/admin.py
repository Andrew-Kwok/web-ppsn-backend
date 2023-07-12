from django.contrib import admin

from . import models

class RegistrationDataAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_at', 'updated_at')
    list_display = ['id', 'nama_lengkap']


class RegistrationDataOrganizationAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )
    list_display = ['id', 'registration_data__nama_lengkap']


class RegistrationDataAchievementAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )
    list_display = ['id', 'registration_data__nama_lengkap']


class RegistrationDataExperienceAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )
    list_display = ['id', 'registration_data__nama_lengkap']
    

class RegistrationDataPublicationAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )
    list_display = ['id', 'registration_data__nama_lengkap']


class RegistrationDataScholarshipAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )
    list_display = ['id', 'registration_data__nama_lengkap']


class RegistrationDataLanguageAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )
    list_display = ['id', 'registration_data__nama_lengkap']


class RegistrationDataSkillAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )
    list_display = ['id', 'registration_data__nama_lengkap']


class RegistrationDataDivisionChoiceAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )
    list_display = ['id', 'registration_data__nama_lengkap']


# Register your models here.
admin.site.register(models.RegistrationData, RegistrationDataAdmin)
admin.site.register(models.RegistrationDataOrganization, RegistrationDataOrganizationAdmin)
admin.site.register(models.RegistrationDataAchievement, RegistrationDataAchievementAdmin)
admin.site.register(models.RegistrationDataExperience, RegistrationDataExperienceAdmin)
admin.site.register(models.RegistrationDataPublication, RegistrationDataPublicationAdmin)
admin.site.register(models.RegistrationDataScholarship, RegistrationDataScholarshipAdmin)
admin.site.register(models.RegistrationDataLanguage, RegistrationDataLanguageAdmin)
admin.site.register(models.RegistrationDataSkill, RegistrationDataSkillAdmin)
admin.site.register(models.RegistrationDataDivisionChoice, RegistrationDataDivisionChoiceAdmin)