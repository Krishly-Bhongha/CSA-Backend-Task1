from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .models import*
from .serializers import*
from .permissions import *
from .services import *

class leaderboardViewSet(viewsets.ViewSet):
    queryset = None
    serializer_class = leaderboardSerializer
    if request.method not in ('GET','RETRIEVE'):
        permission_classes = [IsSuperUser]

    def list(self, request):
        hostels = hostel.objects.all()
        serializer = leaderboardSerializer(hostels, many=True)

        leaderboard = sorted(
        serializer.data,
        key=lambda x: x["score"],
        reverse=True
        )
        return Response(leaderboard)

class HostelViewSet(viewsets.ModelViewSet):
    queryset = hostel.objects.all()
    serializer_class = hostelSerializer
    if request.method in ('POST','PUT','PATCH','DELETE'):
        permission_classes = [IsSuperUser]

class MissionViewSet(viewsets.ModelViewSet):    
    queryset = mission.objects.all()
    serializer_class = missionSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["status", "difficulty", "hostel"]
    search_fields = ["Codename", "brief"]

    if request.method in ('POST','PUT','PATCH','DELETE'):
        permission_classes = [IsSuperUser]

    @action(detail=True, methods=['post'], url_path='expiry', url_name='expiry')
    def check_expiration(self, request, pk=None):
        time = request.data.get('current_time')
        mission = self.get_object()
        return expiration(time, mission)
        
class participantViewSet(viewsets.ModelViewSet):
    queryset = participant.objects.all()
    serializer_class = participantSerializer
    if request.method not in ('POST','GET','RETRIEVE'):
        permission_classes = [IsSelf | IsSuperUser]

    @action(detail=True, methods=['get'], url_path='missions', url_name='missions')
    def get_missions(self, request, pk=None):
        participant = self.get_object()
        time = request.data.get('current_time')
        missions = mission.objects.filter(participant=participant)
        for mission in missions:
            expiration(time, mission)
        serializer = missionSerializer(missions, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'], url_path='claim-mission', url_name='claim-mission')
    def claim_mission(self, request, pk=None):
        participant = self.get_object()
        mission_id = request.data.get('mission_id')
        expiration(request.data.get('current_time'), mission.objects.get(id=mission_id))
        return claim(mission_id, participant)
    
    @action(detail=True, methods=['post'], url_path='complete-mission', url_name='complete-mission')
    def complete_mission(self, request, pk=None):
        participant = self.get_object()
        mission_id = request.data.get('mission_id')
        expiration(request.data.get('current_time'), mission.objects.get(id=mission_id))
        return complete(mission_id, participant)
    
class organiserViewSet(viewsets.ModelViewSet):
    queryset = organiser.objects.all()
    serializer_class = organiserSerializer
    permission_classes = [IsAdmin]

    @action(detail=True, methods=['post'], url_path='missions', url_name='missions')
    def promote_to_admin(self, request, pk=None):
        organiser = self.get_object()
        return promote(organiser)

