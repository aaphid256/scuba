# Django Models for User, Dive, Destination, and DiverProfile

from django.contrib.auth.models import AbstractUser
from django.db import models


# User model
class User(AbstractUser):
    pass


# Model for a Dive
class Dive(models.Model):
    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    date = models.DateField()
    depth = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.DurationField()
    notes = models.TextField(blank=True)


# Model for Dive Destination
class Destination(models.Model):
    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    notes = models.TextField(blank=True)
    dives = models.ManyToManyField(
        'Dive', related_name='destinations', blank=True)

    def __str__(self):
        return self.name


# Model Diver's Profile
class DiverProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    functional_sac_rate = models.DecimalField(
        max_digits=3, decimal_places=1, default=1.0)
    deco_sac_rate = models.DecimalField(
        max_digits=3, decimal_places=1, default=1.0)
    min_gas_sac = models.DecimalField(
        max_digits=3, decimal_places=1, default=1.0)
