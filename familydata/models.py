from django.db import models
from django.conf import settings
# Create your models here.

class Posittion(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Package(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class FamilyApply(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(unique=True, null=True)
    package = models.CharField(max_length=10, choices=(('standart', 'Standart'),
                                                       ('gold', 'Gold'),
                                                       ('vip','Vip')), default='vip')
    news_subscribe = models.BooleanField()
    comment = models.TextField()
    is_active = models.BooleanField(default=True)
    date_apply = models.DateTimeField(auto_now=True)

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