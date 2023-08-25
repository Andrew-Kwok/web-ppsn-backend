from rest_framework import permissions
from .models import UserVotingProfile

class CanVotePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            return request.user.uservotingprofile.can_vote
        except UserVotingProfile.DoesNotExist:
            return False
