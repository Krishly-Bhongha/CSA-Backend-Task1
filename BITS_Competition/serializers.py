from django.http import request
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        if request.method == 'GET':
            fields = ['id', 'first_name', 'last_name', 'email']
        read_only_fields = ['id']
        
class participantSerializer(serializers.ModelSerializer):
    hostel_name = serializers.CharField(source='hostel.name')
    user = UserSerializer()
    class Meta:
        model = participant
        fields = ['id', 'handle', 'hostel_name' , 'user']
        read_only_fields = ['id']

class crackedMissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = mission
        fields = ['id','Codename','points']
        
class hostelSerializer(serializers.ModelSerializer):
    cracked_missions = crackedMissionSerializer(many=True, read_only=True)
    class Meta: 
        model = hostel
        fields = ['id', 'name', 'score','cracked_missions']
        read_only_fields = ['id']

class missionSerializer(serializers.ModelSerializer):
    class Meta:
        model = mission
        hostel_name = serializers.CharField(source='hostel.name')
        participant_handle = serializers.CharField(source='participant.handle')   
        fields = ['id', 'Codename', 'Status', 'Deadline', 'points', 'brief',
                    'Difficulty', 'hostel_name', 'participant_handle']
        read_only_fields = ['id']
            
class organiserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = organiser
        fields = ['id','admin','handle', 'user']
        read_only_fields = ['id']

__all__ = [
    name for name in globals()
    if not name.startswith("_")
    and name not in ("serializers", "User")
]