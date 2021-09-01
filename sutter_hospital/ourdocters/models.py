from django.db import models

# Create your models here.


class Doctors(models.Model):
    name = models.CharField(max_length=10)
    specialization = models.CharField(max_length=10)
    contact = models.CharField(max_length=10)
    time = models.TimeField()
    cabin = models.CharField(max_length=5)
