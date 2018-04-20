from django.db import models
# from

# Create your models here.

class Request(models.Model):
    latitude=models.FloatField(null=False)
    longitude=models.FloatField(null=False)
    number=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    timestamp=models.CharField(max_length=50)

class Ambulance(models.Model):
    latitude=models.FloatField(null=False)
    longitude=models.FloatField(null=False)
    status=models.CharField(max_length=50, null=True, default="PENDING")