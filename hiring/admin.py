from django.contrib import admin

from . import models

class RegistrationDataAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )
    list_display = ['id', 'nama_lengkap']


class RegistrationDataOrganization(admin.ModelAdmin):
    readonly_fields = ('id', )
    list_display = ['id', 'registration_data__nama_lengkap']

# Register your models here.
admin.site.register(models.RegistrationData, RegistrationDataAdmin)
admin.site.register(models.RegistrationDataOrganization, RegistrationDataOrganization)
admin.site.register(models.RegistrationDataAchievement)
admin.site.register(models.RegistrationDataExperience)
admin.site.register(models.RegistrationDataPublication)
admin.site.register(models.RegistrationDataScholarship)
admin.site.register(models.RegistrationDataLanguage)
admin.site.register(models.RegistrationDataSkill)
admin.site.register(models.RegistrationDataDivisionChoice)