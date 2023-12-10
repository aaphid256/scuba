# Django Forms for Model and Non-Model Data

# Import necessary modules
from django import forms
from .models import Dive, Destination, DiverProfile


# Form for Dive Model
class DiveForm(forms.ModelForm):
    class Meta:
        model = Dive
        fields = ['location', 'date', 'depth', 'duration', 'notes']


# Form for Destination Model
class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['name', 'description', 'notes']


# Form for DiverProfile Model
class DiverProfileForm(forms.ModelForm):
    class Meta:
        model = DiverProfile
        fields = ['functional_sac_rate', 'deco_sac_rate', 'min_gas_sac']
