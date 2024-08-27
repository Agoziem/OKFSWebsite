from django.shortcuts import render,redirect
from .models import *
from SRMS.models import Students_Pin_and_ID
from .forms import Contactform
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse
import random

def home_view(request):
	queryset1=School.objects.all()
	queryset2=Management.objects.all()
	queryset3=School.objects.all()[:1]
	queryset4=FAQ.objects.all()
	queryset5=UpcomingEvents.objects.all()
	queryset6=PhotoGallery.objects.all()
	carousel_items = CarouselItem.objects.all()
	
	photos=[]
	homePhotos=[]
	for photoobject in queryset6:
		photos.append(photoobject)
		homePhotos=photos[:6]
	context= {
	'mapbox_private_key':settings.MAPBOXGL_ACCESSTOKEN,
	'schools':queryset1,
	'managements':queryset2,
	'header':queryset3,
	'FAQ':queryset4,
	'events':queryset5,
	'photos':homePhotos,
	'carousel_items': carousel_items
	}
	return render(request,'home.html',context)

def student_card_view(request):
	P = Paginator(Students_Pin_and_ID.objects.all(),21)
	page= request.GET.get('page')
	students = P.get_page(page)
	context = {
        "students":students
    }
	return render(request,'Card_Activation.html',context)


def random_14_digit():
	return str(random.randint(10**13, 10**14 - 1))

def regenerate_all_pin_view(request):
	try:
		for student in Students_Pin_and_ID.objects.all():
			student.student_pin = random_14_digit()
			student.save()
		return JsonResponse({'message':'All pins have been regenerated successfully'}, safe=False)
	except:
		return JsonResponse({'message':'An error occured, please try again later'}, safe=False)

def teachers_view(request):
	queryset= TopTeacher.objects.all()
	context = {
		"Teachers": queryset,
    }
	return render(request, "teachers_data.html", context)
	
def about_view(request):
	queryset3=School.objects.all()[:1]
	context= {
	'header':queryset3,
	}
	return render(request,'about.html',context)

def photo_gallery_view(request):
	Photos=PhotoGallery.objects.all().order_by('-id',)
	context= {
	"photos":Photos,
	}
	return render(request,'photo_gallery.html',context)
	
def home2_view(request):
	if request.method == 'POST':
		emails=request.POST.get('email')
		"""
		subject = "Welcome message"
		message = "thanks for subscribing to our newsletter, you start receiving our newsletter"
		sender=settings.EMAIL_HOST_USER
		recipients = [emails]
		send_mail(subject, message, sender, recipients, fail_silently=False)
		"""
		Subscription.objects.create(Email=emails)
		messages.success(request, 'thanks for subscribing, you will start receiving our newsletters')
		return redirect('home')

def contact_form(request):
	form = Contactform()
	if request.method == 'POST':
		form = Contactform(request.POST)
		if form.is_valid():
			"""
			subject = f'Message from {form.cleaned_data["name"]}'
			message = form.cleaned_data["message"]
			sender=settings.EMAIL_HOST_USER
			email = form.cleaned_data["email"]
			recipients = [email]
			send_mail(subject, message, sender, recipients, fail_silently=False)
			"""
			form.save()
			form = Contactform()
			messages.success(request, 'your feedback have been sent successfully')
			return render(request, 'contact_form.html', {'form': form})
	return render(request, 'contact_form.html', {'form': form})

