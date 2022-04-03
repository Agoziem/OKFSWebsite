from django import forms
from Payments.models import Payment

class PaymentForm2(forms.ModelForm):
	class Meta:
		model = Payment
		fields =[
			'Name_of_student',
            'Payment_type',
            'Email',    
        ]
		widgets={
			'Name_of_student':forms.TextInput(attrs={'class':'form-control'}),
			'Payment_type':forms.Select(attrs={'class':'form-select'}),
			'Email':forms.TextInput(attrs={'class':'form-control'}),
			
        }