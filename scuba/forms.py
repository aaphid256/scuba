from django import forms
from .models import Dive, Destination

class DiveForm(forms.ModelForm):
    class Meta:
        model = Dive
        fields = ['location', 'date', 'depth', 'duration', 'notes']


class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['name', 'description', 'notes']