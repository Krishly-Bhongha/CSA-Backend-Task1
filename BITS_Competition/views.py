from rest_framework import viewsets,status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import*
from .serializers import*

class HostelViewSet(viewsets.ModelViewSet):
    queryset = hostel.objects.all()
    serializer_class = hostelSerializer

class MissionViewSet(viewsets.ModelViewSet):    
    queryset = mission.objects.all()
    serializer_class = missionSerializer
    
class participantViewSet(viewsets.ModelViewSet):
    queryset = participant.objects.all()
    serializer_class = participantSerializer
