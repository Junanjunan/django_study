from django.db import models

# Create your models here.
class Fruits(models.Model):
    name = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    grade = models.PositiveIntegerField()
    group = models.PositiveIntegerField(null=True)


class Shops(models.Model):
    name = models.CharField(max_length=30)
    fruits = models.ManyToManyField(Fruits)



class ShopFake(models.Model):
    no_name = models.CharField(max_length=30)
    no_fruits = models.CharField(max_length=10, null=True)

class ShopFake2(models.Model):
    ok_name = models.IntegerField()
    ok_fruits = models.TextField()

class CharTest(models.Model):
    a = models.CharField(max_length=10)
    b = models.CharField(max_length=10)
    c = models.CharField(max_length=10)
    d = models.CharField(max_length=10)
