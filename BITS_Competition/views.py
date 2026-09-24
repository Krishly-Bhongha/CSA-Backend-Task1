from rest_framework import viewsets,status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import*
from .serializers import*
from .permissions import *

class HostelViewSet(viewsets.ModelViewSet):
    queryset = hostel.objects.all()
    serializer_class = hostelSerializer
    if request.method != 'GET':
        permission_classes = [IsSuperUser]

class MissionViewSet(viewsets.ModelViewSet):    
    queryset = mission.objects.all()
    serializer_class = missionSerializer
    if request.method != 'GET':
        permission_classes = [IsSuperUser]

class participantViewSet(viewsets.ModelViewSet):
    queryset = participant.objects.all()
    serializer_class = participantSerializer
    if request.method not in ('GET','POST'):
        permission_classes = [IsSuperUser]
    @action(detail=True, methods=['get'], url_path='missions', url_name='missions')

    def get_missions(self, request, pk=None):
        participant = self.get_object()
        missions = mission.objects.filter(participant=participant)
        serializer = missionSerializer(missions, many=True)
        return Response(serializer.data)
    
    def complete_mission(self, request, pk=None):
        participant = self.get_object()
        mission_id = request.data.get('mission_id')
        try:
            mission = mission.objects.get(id=mission_id)
        except mission.DoesNotExist:
            return Response({'error': 'Mission not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if mission.participant != participant:
            return Response({'error': 'This mission is not assigned to this participant'}, status=status.HTTP_400_BAD_REQUEST)
        
        if mission.Status == 'cracked':
            return Response({'error': 'This mission is already completed'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Mark the mission as completed
        mission.Status = 'Completed'
        mission.save()
        
        # Update the hostel's score
        participant.hostel.score += mission.points
        participant.hostel.save()
        participant.hostel.crcked_missions.add(mission)
        
        return Response({'message': 'Mission completed successfully'}, status=status.HTTP_200_OK)
    
class organiserViewSet(viewsets.ModelViewSet):
    queryset = organiser.objects.all()
    serializer_class = organiserSerializer
    permission_classes = [IsAdmin]