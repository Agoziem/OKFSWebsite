from django.shortcuts import render,redirect
from .models import PhotoGallery,School,Management,Subscription,Header,FAQ,UpcomingEvents,Contact
from .forms import Contactform
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages

def home_view(request):
	queryset1=School.objects.all()
	queryset2=Management.objects.all()
	queryset3=Header.objects.all()
	queryset4=FAQ.objects.all()
	queryset5=UpcomingEvents.objects.all()
	queryset6=PhotoGallery.objects.all()
	
	photos=[]
	homePhotos=[]
	for photoobject in queryset6:
		photos.append(photoobject)
		homePhotos=photos[:6]
	context= {
	'mapbox_private_key':settings.MAPBOXGL.ACCESSTOKEN
	'schools':queryset1,
	'managements':queryset2,
	'headers':queryset3,
	'FAQ':queryset4,
	'events':queryset5,
	'photos':homePhotos,
	}
	return render(request,'home.html',context)
	
def about_view(request):
	queryset3=Header.objects.all()
	context= {
	'headers':queryset3,
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
		messages.success(request, 'thanks for subscribing to our newsletter, you will start receiving our newsletters')
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

