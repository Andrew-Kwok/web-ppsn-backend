from django.contrib import admin

from .models import (
    Candidate,
    UserVotingProfile,
)

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'votes')
    list_display = ['id', 'name', 'votes']

@admin.register(UserVotingProfile)
class UserVotingProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'can_vote', 'voted_candidate']