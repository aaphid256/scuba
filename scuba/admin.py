# Django Admin Page Configuration

# Import necessary modules
from django.contrib import admin
from .models import Dive, Destination, DiverProfile

# Register your models here.
admin.site.register(Dive)
admin.site.register(Destination)
admin.site.register(DiverProfile)
