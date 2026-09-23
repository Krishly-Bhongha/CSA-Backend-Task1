from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name','last_name', 'email']
        
class participantSerializer(serializers.ModelSerializer):
    hostel_name = serializers.CharField(source='hostel.name', read_only=True)
    user = UserSerializer(read_only=True)
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

__all__ = [
    name for name in globals()
    if not name.startswith("_")
    and name not in ("serializers", "User")
]