from django.db import models
from datetime import datetime

def custom_upload_to():
    return datetime.now()

class Home(models.Model):
    title = models.CharField(max_length=30)
    banner = models.ImageField(upload_to=custom_upload_to(), null=True)