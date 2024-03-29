from django.shortcuts import render,get_object_or_404,redirect
from .forms import PaymentForm2
from .models import Student
from Payments.models import Payment,Amount
from django.conf import settings
from .forms import PaymentForm2
import base64
base64.encodestring = base64.encodebytes
base64.decodestring = base64.decodebytes
from django.http import HttpResponse
from django.contrib import messages
from home.models import School

def initiate_payment2(request):
	if request.method=='POST':
		Payment_form=PaymentForm2(request.POST)
		if Payment_form.is_valid():
			Payment=Payment_form.save()
			amount=Amount.objects.get(description =Payment.Payment_type)
			context={
			'payment': Payment,
			'paymentamount': amount,
			'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY
			}
			return render(request,'Make_payment2.html',context)
	else:
		payment_form=PaymentForm2()
		return render(request,'Initiate_payment2.html', { 'form':payment_form })

def verify_payment2(request , ref : str) -> HttpResponse:
	payment=get_object_or_404(Payment,ref=ref)
	amount=get_object_or_404(Amount,description=payment.Payment_type)
	verified=payment.verify_payment()
	if verified:
		messages.success(request,"payment successful")
		return render(request, 'Admission_form.html', { "receipt": payment , "paidamount": amount })
	else:
		messages.error(request,"verification failed, check your inputs and try again") 
		return redirect('Initiate_payment2.html')
		
def admission_details(request):
	if request.method=='POST':
		FirstName=request.POST.get('FirstName')
		LastName=request.POST.get('LastName')
		Address=request.POST.get('Address')
		Town=request.POST.get('Town')
		LGA=request.POST.get('LGA')
		State_of_Origin=request.POST.get('State_of_Origin')
		Nationality=request.POST.get('Nationality')
		Religion=request.POST.get('Religion')
		School_attended=request.POST.get('School_attended')
		last_Class_passed=request.POST.get('last_Class_passed')
		Common_Ent_Exam_Number=request.POST.get('Common_Ent_Exam_Number')
		Agg_Score=request.POST.get('Agg_Score')
		Class_applying_for=request.POST.get('Class_applying_for')
		Disability=request.POST.get('Disability')
		Specify=request.POST.get('Specify')
		I_certify_that_the_information_given_above_are_the_truth_and_nothing_but_the_truth=request.POST.get('I_certify_that_the_information_given_above_are_the_truth_and_nothing_but_the_truth',"True")
		Parents_Name=request.POST.get('Parents_Name')
		Addressp=request.POST.get('Addressp')
		Phone_numberp=request.POST.get('Phone_numberp')
		Townp=request.POST.get('Townp')
		LGAp=request.POST.get('LGAp')
		State_of_Originp=request.POST.get('State_of_Originp')
		are_you_ready_to_cooperate_with_the_School_or_PTA_for_the_proper_upbringing_of_your_Child=request.POST.get('are_you_ready_to_cooperate_with_the_School_or_PTA_for_the_proper_upbringing_of_your_Child')
		are_you_ready_to_pay_all_the_approved_fees_as_at_when_due=request.POST.get('are_you_ready_to_pay_all_the_approved_fees_as_at_when_due')
		is_your_Child_ready_to_obey_all_the_school_Rules_and_Regulations=request.POST.get('is_your_Child_ready_to_obey_all_the_school_Rules_and_Regulations')
		
		student=Student.objects.create(
			firstName=FirstName,
			lastName=LastName,
			address=Address,
			town=Town,
			lGA=LGA,
			state_of_Origin=State_of_Origin,
			nationality=Nationality,
			religion=Religion,
			school_attended=School_attended,
			Last_Class_passed=last_Class_passed,
			common_Ent_Exam_Number=Common_Ent_Exam_Number,
			agg_Score=Agg_Score,
			class_applying_for=Class_applying_for,
			disability=Disability,
			specify=Specify,
			certify=I_certify_that_the_information_given_above_are_the_truth_and_nothing_but_the_truth,
			parents_Name=Parents_Name,
			addressp=Addressp,
			phone_numberp=Phone_numberp,
			townp=Townp,
			lGAp=LGAp,
			state_of_Originp=State_of_Originp,
			question_1=are_you_ready_to_cooperate_with_the_School_or_PTA_for_the_proper_upbringing_of_your_Child,
			question_2=are_you_ready_to_pay_all_the_approved_fees_as_at_when_due,
			question_3=is_your_Child_ready_to_obey_all_the_school_Rules_and_Regulations,
				)
		school=School.objects.all()
		context={
		"object":student,
		"school":school,
		}
		return render(request, 'Admission_details.html', context)
	

	# I deleted the View for the PDF, because we are now using jspdf for the Purpose of Printing PDF

