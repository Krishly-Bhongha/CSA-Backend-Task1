from rest_framework.decorators import action

from .models import*
from .serializers import*
from .permissions import *
from .services import *

class HostelViewSet(viewsets.ModelViewSet):
    queryset = hostel.objects.all()
    serializer_class = hostelSerializer
    if request.method in ('POST','PUT','PATCH','DELETE'):
        permission_classes = [IsSuperUser]

class MissionViewSet(viewsets.ModelViewSet):    
    queryset = mission.objects.all()
    serializer_class = missionSerializer
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
    if request.method not in ('POST','GET'):
        permission_classes = [IsSelf | IsSuperUser]
    
    @action(detail=True, methods=['post'], url_path='claim-mission', url_name='claim-mission')
    def claim_mission(self, request, pk=None):
        participant = self.get_object()
        mission_id = request.data.get('mission_id')
        return claim(mission_id, participant)
    
    @action(detail=True, methods=['post'], url_path='complete-mission', url_name='complete-mission')
    def complete_mission(self, request, pk=None):
        participant = self.get_object()
        mission_id = request.data.get('mission_id')
        return complete(mission_id, participant)
    
class organiserViewSet(viewsets.ModelViewSet):
    queryset = organiser.objects.all()
    serializer_class = organiserSerializer
    permission_classes = [IsAdmin]

    @action(detail=True, methods=['post'], url_path='missions', url_name='missions')
    def promote_to_admin(self, request, pk=None):
        organiser = self.get_object()
        return promote(organiser)

