from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    registration = models.DateField(auto_now=True)

