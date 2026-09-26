from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class hostel(models.Model):
    name = models.CharField(max_length=100)

class organiser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    handle = models.CharField(max_length=100)
    admin = models.BooleanField(default=False)

class participant(models.Model):
    handle = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hostel = models.ForeignKey(hostel, on_delete=models.CASCADE)

class mission(models.Model):
    brief = models.TextField()
    points = models.IntegerField()
    Codename = models.CharField(max_length=100)
    Difficulty = models.IntegerField()
    Status = models.CharField(max_length=100)
    Deadline = models.DateTimeField()
    participant = models.ForeignKey(participant, on_delete=models.DO_NOTHING, null=True, blank=True,default=None)

__all__ = [
    name for name in globals()
    if not name.startswith("_")
    and name not in ("models", "User")
]


    