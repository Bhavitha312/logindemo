from django.db import models

# Create your models here.

class Std(models.Model):
    name=models.CharField(null=False, max_length=100)
    lastname=models.CharField(null=False, max_length=100)
    password=models.CharField(null=False, max_length=20)
