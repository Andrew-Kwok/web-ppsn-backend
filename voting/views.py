from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Candidate
from .serializers import CandidateSerializer
from .permissions import CanVotePermission

class CandidateListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        candidates = Candidate.objects.all()
        serializer = CandidateSerializer(candidates, many=True)
        return Response(serializer.data)

class VoteView(APIView):
    permission_classes = [permissions.IsAuthenticated, CanVotePermission]

    def post(self, request):
        candidate_id = request.data.get('candidate_id')

        try:
            candidate = Candidate.objects.get(pk=candidate_id)
        except Candidate.DoesNotExist:
            return Response({'detail': 'Invalid candidate ID.'}, status=status.HTTP_400_BAD_REQUEST)

        user_profile = request.user.uservotingprofile

        if user_profile.voted_candidate:
            return Response({'detail': 'You have already voted for a candidate.'}, status=status.HTTP_400_BAD_REQUEST)


        user_profile.voted_candidate = candidate
        candidate.votes += 1

        user_profile.can_vote = False
        user_profile.save()
        candidate.save()

        return Response({'detail': 'Vote cast successfully.'}, status=status.HTTP_201_CREATED)
