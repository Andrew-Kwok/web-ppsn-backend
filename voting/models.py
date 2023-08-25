from django.db import models
from django.contrib.auth.models import User

class Candidate(models.Model):
    name = models.CharField(max_length=255)
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    
class UserVotingProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    can_vote = models.BooleanField(default=False)
    voted_candidate = models.ForeignKey(Candidate, related_name='voted_candidate', blank=True, null=True, on_delete=models.CASCADE)

