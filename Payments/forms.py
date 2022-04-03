from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
	class Meta:
		model = Payment
		fields =[
			'Name_of_student',
            'Class',
            'Payment_type',
            'Email',    
        ]
		widgets={
			'Name_of_student':forms.TextInput(attrs={'class':'form-control'}),
			'Class':forms.Select(attrs={'class':'form-select'}),
			'Payment_type':forms.Select(attrs={'class':'form-select'}),
			'Email':forms.TextInput(attrs={'class':'form-control'}),
			
        }