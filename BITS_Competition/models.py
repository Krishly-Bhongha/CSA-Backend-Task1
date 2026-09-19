from django.db import models
from django.contrib.auth.models import User

# Create your models here.
hostels= ("Ram","budh","Shankar","Vyas","Meera",
         "Krishna","Gandhi","Ashok","Malviya","CVR","SR",
         "RP","VK","Bhagirath") # I can't seem to find remaining 3 hostels

statuses = ("unclaimed","in_progress","cracked","expired")

class hostel(models.Model):
    name = models.CharField(choices=((h, h) for h in hostels), max_length=100)

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
    Status = models.CharField(choices=((s, s) for s in statuses), max_length=100,default="unclaimed")
    Deadline = models.DateTimeField()
    participant = models.ForeignKey(participant, on_delete=models.DO_NOTHING, null=True, blank=True,default=None)




    