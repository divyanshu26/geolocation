from django.contrib import admin
from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    latitude = models.FloatField()
    longitude = models.FloatField()
    accuracy = models.FloatField()

    def __str__(self):
        return self.name