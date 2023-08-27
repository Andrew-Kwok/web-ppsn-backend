from rest_framework import serializers
from .models import Candidate, UserVotingProfile

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['id', 'name', 'votes']


class UserVotingProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserVotingProfile
        fields = ['can_vote']
