from django.db import models

# Create your models here.
class CallFruits(models.Model):
    name = models.CharField(max_length=20)
    fruits = models.ForeignKey("fruits.Fruits", on_delete=models.CASCADE)
    shops = models.ManyToManyField("fruits.Shops")