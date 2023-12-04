from django import forms
from .models import *

class Contactform(forms.ModelForm):
	class Meta:
		model = Contact
		fields =[
			'name',
            'message',
            'email',   
        ]
		widgets={
			'name':forms.TextInput(attrs={'class':'form-control'}),
			'message':forms.Textarea(attrs={'class':'form-control'}),
			'email':forms.TextInput(attrs={'class':'form-control'}),
        }