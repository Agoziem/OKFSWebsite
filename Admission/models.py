from django.db import models
from Payments.models import Amount
from Payments.Paystack import Paystack

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
	i_certify_that_the_information_given_above_are_the_truth_and_nothing_but_the_truth=models.BooleanField(default=False,blank=True)
	parents_Name=models.CharField(max_length=100, blank=True)
	addressp=models.CharField(max_length=100, blank=True)
	phone_numberp=models.CharField(max_length=100, blank=True)
	townp=models.CharField(max_length=100, blank=True)
	lGAp=models.CharField(max_length=100, blank=True)
	state_of_Originp=models.CharField(max_length=100, blank=True)
	Are_you_ready_to_cooperate_with_the_School_or_PTA_for_the_proper_upbringing_of_your_Child=models.CharField(max_length=100, choices=boolChoice, blank=True)
	Are_you_ready_to_pay_all_the_approved_fees_as_at_when_due=models.CharField(max_length=100, blank=True,choices=boolChoice)
	Is_your_Child_ready_to_obey_all_the_school_Rules_and_Regulations=models.CharField(max_length=100, blank=True, choices=boolChoice)
	Admitted=models.BooleanField(default=False,blank=True)
	
	