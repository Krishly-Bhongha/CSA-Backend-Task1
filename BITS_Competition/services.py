from rest_framework.response import Response
from rest_framework import viewsets,status
from .models import*

def expiration(time, mission):
    if mission.Deadline < time:
        mission.Status = 'expired'
        mission.save()
        return Response({'message': 'Mission expired'}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Mission still active'}, status=status.HTTP_200_OK)

def complete(mission_id, participant):
    try:
        mission = mission.objects.get(id=mission_id)
    except mission.DoesNotExist:
        return Response({'error': 'Mission not found'}, status=status.HTTP_404_NOT_FOUND)

    if mission.participant != participant:
        return Response({'error': 'This mission is not assigned to this participant'}, status=status.HTTP_400_BAD_REQUEST)
    
    if mission.Status == 'cracked':
        return Response({'error': 'This mission is already completed'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Mark the mission as completed
    mission.Status = 'cracked'
    mission.save()
    
    return Response({'message': 'Mission completed successfully'}, status=status.HTTP_200_OK)

def claim(mission_id, participant):
    try:
        mission = mission.objects.get(id=mission_id)
    except mission.DoesNotExist:
        return Response({'error': 'Mission not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if mission.Status in ('in_progress','cracked'):
        return Response({'error': 'This mission is already claimed/cracked by another participant'}, status=status.HTTP_400_BAD_REQUEST)
    
    if mission.Status == 'expired':
        return Response({'error': 'This mission is expired'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Assign the mission to the participant
    mission.participant = participant
    mission.Status = 'in_progress'
    mission.save()
    
    return Response({'message': 'Mission claimed successfully'}, status=status.HTTP_200_OK)

def promote(organiser):
    organiser.admin = True
    organiser.save()
    return Response({'message': 'Organiser promoted to admin successfully'}, status=status.HTTP_200_OK)