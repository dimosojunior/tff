from DimosoApp.models import *
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

class TeamForm(forms.ModelForm):
	prayer_name = forms.CharField(
		required=True,
		label=False,
		widget=forms.TextInput(attrs={'id' :'prayer_name', 'placeholder' : 'Enter Player Name'})

	)
	team_name = forms.CharField(
		required=True,
	#label=False,
		widget=forms.TextInput(attrs={'placeholder' : 'Enter Team Name'})

	)



	class Meta:
		model = TeamInformations
		fields = '__all__'
class ResultsForm(forms.ModelForm):
	



	class Meta:
		model = Results
		fields = '__all__'

class RatibaForm(forms.ModelForm):
	



	class Meta:
		model = Ratiba
		fields = '__all__'
class MsimamoForm(forms.ModelForm):
	



	class Meta:
		model = Msimamo
		fields = '__all__'