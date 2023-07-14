from django.contrib import admin
from .models import (
    RegistrationData,
    RegistrationDataOrganization,
    RegistrationDataAchievement,
    RegistrationDataExperience,
    RegistrationDataScholarship,
    RegistrationDataPublication,
    RegistrationDataLanguage,
    RegistrationDataSkill,
    RegistrationDataDivisionChoice,
    RegistrationDataCommitteeDecision,
)

class RegistrationDataOrganizationInline(admin.TabularInline):
    model = RegistrationDataOrganization
    extra = 0

class RegistrationDataAchievementInline(admin.TabularInline):
    model = RegistrationDataAchievement
    extra = 0

class RegistrationDataExperienceInline(admin.TabularInline):
    model = RegistrationDataExperience
    extra = 0

class RegistrationDataScholarshipInline(admin.TabularInline):
    model = RegistrationDataScholarship
    extra = 0

class RegistrationDataPublicationInline(admin.TabularInline):
    model = RegistrationDataPublication
    extra = 0

class RegistrationDataLanguageInline(admin.TabularInline):
    model = RegistrationDataLanguage
    extra = 0

class RegistrationDataSkillInline(admin.TabularInline):
    model = RegistrationDataSkill
    extra = 0

class RegistrationDataDivisionChoiceInline(admin.TabularInline):
    model = RegistrationDataDivisionChoice
    extra = 0

class RegistrationDataCommitteeDecisionInline(admin.TabularInline):
    model = RegistrationDataCommitteeDecision
    extra = 0

@admin.register(RegistrationData)
class RegistrationDataAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_at', 'updated_at')
    list_display = ['id', 'nama_lengkap', 'tanggal_lahir', 'created_at', 'committee_decision_nama_panitia', 'committee_decision_berkas_lengkap', 'committee_decision_status_lulus']
    ordering = ['-created_at']
    inlines = [
        RegistrationDataOrganizationInline,
        RegistrationDataAchievementInline,
        RegistrationDataExperienceInline,
        RegistrationDataScholarshipInline,
        RegistrationDataPublicationInline,
        RegistrationDataLanguageInline,
        RegistrationDataSkillInline,
        RegistrationDataDivisionChoiceInline,
        RegistrationDataCommitteeDecisionInline,
    ]

    def committee_decision_nama_panitia(self, obj):
        return obj.hasil_seleksi.nama_panitia if obj.hasil_seleksi else 'Unassigned'
    committee_decision_nama_panitia.short_description = 'Nama Panitia'


    def committee_decision_berkas_lengkap(self, obj):
        return obj.hasil_seleksi.berkas_lengkap if obj.hasil_seleksi else ''
    committee_decision_berkas_lengkap.short_description = 'Berkas Lengkap'

    def committee_decision_status_lulus(self, obj):
        return obj.hasil_seleksi.status_lulus if obj.hasil_seleksi else ''
    committee_decision_status_lulus.short_description = 'Status Lulus'



# class RegistrationDataOrganizationAdmin(admin.ModelAdmin):
#     readonly_fields = ('id', 'registration_data')
#     list_display = ['id', 'registration_data__nama_lengkap', 'registration_data__tanggal_lahir']


# class RegistrationDataAchievementAdmin(admin.ModelAdmin):
#     readonly_fields = ('id', 'registration_data')
#     list_display = ['id', 'registration_data__nama_lengkap', 'registration_data__tanggal_lahir']


# class RegistrationDataExperienceAdmin(admin.ModelAdmin):
#     readonly_fields = ('id', 'registration_data')
#     list_display = ['id', 'registration_data__nama_lengkap', 'registration_data__tanggal_lahir']
    

# class RegistrationDataPublicationAdmin(admin.ModelAdmin):
#     readonly_fields = ('id', 'registration_data')
#     list_display = ['id', 'registration_data__nama_lengkap', 'registration_data__tanggal_lahir']


# class RegistrationDataScholarshipAdmin(admin.ModelAdmin):
#     readonly_fields = ('id', 'registration_data')
#     list_display = ['id', 'registration_data__nama_lengkap', 'registration_data__tanggal_lahir']


# class RegistrationDataLanguageAdmin(admin.ModelAdmin):
#     readonly_fields = ('id', 'registration_data')
#     list_display = ['id', 'registration_data__nama_lengkap', 'registration_data__tanggal_lahir']


# class RegistrationDataSkillAdmin(admin.ModelAdmin):
#     readonly_fields = ('id', 'registration_data')
#     list_display = ['id', 'registration_data__nama_lengkap', 'registration_data__tanggal_lahir']


# class RegistrationDataDivisionChoiceAdmin(admin.ModelAdmin):
#     readonly_fields = ('id', 'registration_data')
#     list_display = ['id', 'registration_data__nama_lengkap', 'registration_data__tanggal_lahir']


# class RegistrationDataDivisionCommitteeDecisionAdmin(admin.ModelAdmin):
#     readonly_fields = ('id', 'registration_data')
#     list_display = ['id', 'registration_data__nama_lengkap', 'registration_data__tanggal_lahir']


# Register your models here.
# admin.site.register(RegistrationData, RegistrationDataAdmin)
# admin.site.register(RegistrationDataOrganization, RegistrationDataOrganizationAdmin)
# admin.site.register(RegistrationDataAchievement, RegistrationDataAchievementAdmin)
# admin.site.register(RegistrationDataExperience, RegistrationDataExperienceAdmin)
# admin.site.register(RegistrationDataPublication, RegistrationDataPublicationAdmin)
# admin.site.register(RegistrationDataScholarship, RegistrationDataScholarshipAdmin)
# admin.site.register(RegistrationDataLanguage, RegistrationDataLanguageAdmin)
# admin.site.register(RegistrationDataSkill, RegistrationDataSkillAdmin)
# admin.site.register(RegistrationDataDivisionChoice, RegistrationDataDivisionChoiceAdmin)
# admin.site.register(RegistrationDataCommitteeDecision, RegistrationDataDivisionCommitteeDecisionAdmin)