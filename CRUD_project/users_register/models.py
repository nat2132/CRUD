from django.db import models

# Create your models here.


class Users(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    password = models.CharField(max_length=8)