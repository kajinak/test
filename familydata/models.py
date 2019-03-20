from django.db import models
from django.conf import settings
# Create your models here.

class Posittion(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Family(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=64, null=True, blank=True)
    posittion = models.ForeignKey(Posittion,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name