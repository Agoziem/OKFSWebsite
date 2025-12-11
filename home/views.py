from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from SRMS.models import AcademicSession, StudentClassEnrollment, Students_Pin_and_ID
from .forms import Contactform
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
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
	documents = SchoolDocument.objects.all()
	
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
	'carousel_items': carousel_items,
	'documents': documents,
	}
	return render(request,'home.html',context)

def student_card_view(request):
	# Fetch the academic session dynamically or fall back to a default
    session = request.GET.get("session", "2025/2026")  # Allow session to be passed as a query parameter
    sessionobject = get_object_or_404(AcademicSession, session=session)
    
    # Filter enrolled students for the given session
    studentenrollment = StudentClassEnrollment.objects.filter(academic_session=sessionobject)
    
    # Prepare the list of student details
    students_list = [
        {
            "student_name": enrollment.student.student_name,
            "student_id": enrollment.student.student_id,
            "student_pin": enrollment.student.student_pin,
            "student_class": enrollment.student_class.Class,
        }
        for enrollment in studentenrollment
    ]
    
    # Paginate the filtered student list
    paginator = Paginator(students_list, 21)  # Show 21 students per page
    page = request.GET.get("page")
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)

    # Context for the template
    context = {
        "students": students
    }
    return render(request, "Card_Activation.html", context)


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

