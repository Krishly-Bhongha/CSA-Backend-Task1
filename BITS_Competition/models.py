from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class hostel(models.Model):
    name = models.CharField(max_length=100)

class participant(models.Model):
    handle = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hostel = models.ForeignKey(hostel, on_delete=models.CASCADE)

class mission(models.Model):
    name = models.CharField(max_length=100)
    brief = models.TextField()
    points = models.IntegerField()
    Codename = models.CharField(max_length=100)
    Difficulty = models.IntegerField()
    Status = models.CharField(max_length=100)
    Deadline = models.DateTimeField()
    participant = models.ForeignKey(participant, on_delete=models.DO_NOTHING, null=True, blank=True,default=None)




    