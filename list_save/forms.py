from django import forms
from .models import Lists

class Create(forms.Form):
	username = forms.CharField(max_length=50)
	email = forms.EmailField()
	class Meta:
		model = Lists