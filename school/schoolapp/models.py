from django.db import models

# Create your models here.
class Registrationdata(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    Email = models.EmailField(max_length=100)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    mobile = models.BigIntegerField()
class login_page(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

