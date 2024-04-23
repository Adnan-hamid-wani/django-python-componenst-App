from django.db import models


# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=88)
    email= models.EmailField()
class User(models.Model):
    objects = None
    username=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)