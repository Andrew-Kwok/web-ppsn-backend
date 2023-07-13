from django.contrib import admin

from . import models

class RegistrationDataAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_at', 'updated_at')
    list_display = ['id', 'nama_lengkap', 'tanggal_lahir']


class RegistrationDataOrganizationAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'registration_data')
    list_display = ['id', 'registration_data__nama_lengkap', 'registration_data__tanggal_lahir']


class RegistrationDataAchievementAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'registration_data')
    list_display = ['id', 'registration_data__nama_lengkap', 'registration_data__tanggal_lahir']


class RegistrationDataExperienceAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'registration_data')
    list_display = ['id', 'registration_data__nama_lengkap', 'registration_data__tanggal_lahir']
    

class RegistrationDataPublicationAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'registration_data')
    list_display = ['id', 'registration_data__nama_lengkap', 'registration_data__tanggal_lahir']


class RegistrationDataScholarshipAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'registration_data')
    list_display = ['id', 'registration_data__nama_lengkap', 'registration_data__tanggal_lahir']


class RegistrationDataLanguageAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'registration_data')
    list_display = ['id', 'registration_data__nama_lengkap', 'registration_data__tanggal_lahir']


class RegistrationDataSkillAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'registration_data')
    list_display = ['id', 'registration_data__nama_lengkap', 'registration_data__tanggal_lahir']


class RegistrationDataDivisionChoiceAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'registration_data')
    list_display = ['id', 'registration_data__nama_lengkap', 'registration_data__tanggal_lahir']


class RegistrationDataDivisionCommitteeDecisionAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'registration_data')
    list_display = ['id', 'registration_data__nama_lengkap', 'registration_data__tanggal_lahir']


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
admin.site.register(models.RegistrationDataCommitteeDecision, RegistrationDataDivisionCommitteeDecisionAdmin)