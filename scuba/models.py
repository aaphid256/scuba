from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Dive(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    date = models.DateField()
    depth = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.DurationField()
    notes = models.TextField(blank=True)


class Destination(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    notes = models.TextField(blank=True)
    dives = models.ManyToManyField('Dive', related_name='destinations', blank=True)

    def __str__(self):
        return self.name
    

class DiverProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    functional_sac_rate = models.DecimalField(max_digits=3, decimal_places=1, default=1.0)
    deco_sac_rate = models.DecimalField(max_digits=3, decimal_places=1, default=1.0)
    min_gas_sac = models.DecimalField(max_digits=3, decimal_places=1, default=1.0)