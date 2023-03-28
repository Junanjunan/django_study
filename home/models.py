from django.db import models
from django.utils import timezone
from datetime import datetime

def custom_upload_to():
    return datetime.now()

class Home(models.Model):
    title = models.CharField(max_length=30)
    test_json = models.JSONField(null=True)
    furniture = models.ManyToManyField('Funiture')
    # now = models.DateTimeField(timezone.now)
    staying_time = models.TimeField(null=True)


class Owner(models.Model):
    home = models.OneToOneField(Home, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


class Funiture(models.Model):
    name = models.CharField(max_length=50)
