from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)


class K9(models.Model):
    name = models.CharField(default="champ", max_length=20)
    breed = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    size = models.CharField(default=50, max_length=6)
    gender = models.CharField(default=50, max_length=6)
