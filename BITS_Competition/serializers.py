from rest_framework import serializers
from .models import participant, hostel, organiser, participant, mission

class participantSerializer(serializers.ModelSerializer):
    hostel_name = serializers.CharField(source='hostel.name', read_only=True)
    class Meta:
        model = participant
        fields = ['id', 'handle', 'user', 'hostel', 'hostel_name']
        
class crackedMissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = mission
        fields = ['id','Codename','points']
        read_only_fields = ['id','Codename','points']

class hostelSerializer(serializers.ModelSerializer):
    cracked_missions = crackedMissionSerializer(many=True, read_only=True)
    class Meta:
        model = hostel
        fields = ['id', 'name', 'score','cracked_missions']

class missionSerializer(serializers.ModelSerializer):
    class Meta:
        model = mission
        hostel_name = serializers.CharField(source='hostel.name', read_only=True)
        participant_handle = serializers.CharField(source='participant.handle', read_only=True)
        fields = ['id', 'brief', 'points', 'Codename', 'Difficulty', 'Status', 'Deadline', 'participant_handle','hostel_name']    
