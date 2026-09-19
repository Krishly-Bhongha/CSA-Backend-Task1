from django.db import models

# Create your models here.
hostels=["Ram","budh","Shankar","Vyas","Meera",
         "Krishna","Gandhi","Ashok","Malviya","CVR","SR",
         "RP","VK","Bhagirath"]

class participant(models.Model):
    name = models.CharField(max_length=100)
    handle = models.CharField(max_length=100)
    hostel = models.ForeignKey(hostel, on_delete=models.CASCADE)
    
class hostel(models.Model):
    name = models.CharField(max_length=100)

class mission(models.Model):
    name = models.CharField(max_length=100)
    brief = models.TextField()
    points = models.IntegerField()
    Codename = models.CharField(max_length=100)
    Difficulty = models.IntegerField()
    Status = models.CharField(max_length=100)
    Deadline = models.DateTimeField()
    hostel = models.ForeignKey(hostel, on_delete=models.CASCADE)
    