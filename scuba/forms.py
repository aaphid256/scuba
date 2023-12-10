from django import forms
from .models import Dive, Destination, DiverProfile

class DiveForm(forms.ModelForm):
    class Meta:
        model = Dive
        fields = ['location', 'date', 'depth', 'duration', 'notes']


class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['name', 'description', 'notes']


class DiverProfileForm(forms.ModelForm):
    class Meta:
        model = DiverProfile
        fields = ['functional_sac_rate', 'deco_sac_rate', 'min_gas_sac']        


class BackgasForm(forms.Form):
    cu_ft = forms.FloatField()
    pressure = forms.FloatField()
    fill_pressure = forms.FloatField()

class DecoGasForm(forms.Form):
    cu_ft = forms.FloatField()
    pressure = forms.FloatField()
    fill_pressure = forms.FloatField()

class DivePlannerForm(forms.Form):
    max_depth = forms.FloatField()
    functional_sac_rate = forms.FloatField()
    deco_sac_rate = forms.FloatField()
    min_gas_sac = forms.FloatField()
    rock_bottom_time = forms.FloatField()
    backgas_tanks = forms.IntegerField(min_value=0)
    deco_gasses = forms.ChoiceField(choices=[(i, i) for i in range(3)])


