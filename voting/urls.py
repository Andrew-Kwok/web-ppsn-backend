from django.urls import path
from .views import CandidateListView, VoteView

urlpatterns = [
    path('candidates/', CandidateListView.as_view(), name='candidate-list'),
    path('vote/', VoteView.as_view(), name='vote'),
]
