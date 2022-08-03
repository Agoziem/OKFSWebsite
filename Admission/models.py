from django.db import models
from Payments.models import Amount
from Payments.Paystack import Paystack
# God
boolChoice = (
		("Yes","Yes"),("No","No")
		)

class Student(models.Model):
	firstName=models.CharField(max_length=100, blank=True)
	lastName=models.CharField(max_length=100, blank=True)
	address=models.CharField(max_length=100, blank=True)
	town=models.CharField(max_length=100, blank=True)
	lGA=models.CharField(max_length=100, blank=True)
	state_of_Origin=models.CharField(max_length=100, blank=True)
	nationality=models.CharField(max_length=100, blank=True)
	religion=models.CharField(max_length=100, blank=True)
	school_attended=models.CharField(max_length=100, blank=True)
	Last_Class_passed=models.CharField(max_length=100, blank=True)
	common_Ent_Exam_Number=models.CharField(max_length=100, blank=True,null=True)
	agg_Score=models.CharField(max_length=100, blank=True,null=True)
	class_applying_for=models.CharField(max_length=100, blank=True)
	disability=models.CharField(max_length=100, choices=boolChoice, blank=True) 
	specify=models.CharField(max_length=200, blank=True,null=True)
	certify=models.BooleanField(default=False,blank=True)
	parents_Name=models.CharField(max_length=100, blank=True)
	addressp=models.CharField(max_length=100, blank=True)
	phone_numberp=models.CharField(max_length=100, blank=True)
	townp=models.CharField(max_length=100, blank=True)
	lGAp=models.CharField(max_length=100, blank=True)
	state_of_Originp=models.CharField(max_length=100, blank=True)
	question_1=models.CharField(max_length=100, choices=boolChoice, blank=True)
	question_2=models.CharField(max_length=100, blank=True,choices=boolChoice)
	question_3=models.CharField(max_length=100, blank=True, choices=boolChoice)
	Admitted=models.BooleanField(default=False,blank=True)
	
	