from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Result,Student,Excelfiles,Class,Newsletter,Pin
from home.models import School
from django.contrib.auth.decorators import login_required
import base64
base64.encodestring = base64.encodebytes
base64.decodestring = base64.decodebytes
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.contrib import messages

def classes_view(request):
	queryset= Class.objects.all()
	context = {
		"classes": queryset,
    }
	return render(request, "Classes.html", context)
	
def students_view(request,Classname):
	queryset=Student.objects.filter(Class=Classname)
	queryset2=Class.objects.get(Class=Classname)
	context = {
		"students": queryset,
		"class":queryset2
    }
	return render(request, "Students.html", context)
	
def result_view(request,Classname):
	queryset=Student.objects.filter(Class=Classname)
	queryset2=Class.objects.get(Class=Classname)
	stuff=get_object_or_404(Student,Name=request.POST.get('Name'))
	queryset3=Result.objects.filter(Name=request.POST.get('Name'),Class=Classname)
	letter=Newsletter.objects.all()
	school=School.objects.all()
	if request.method=='POST':
		try:
			enteredpin=request.POST.get('Pin')
			mainpin=int(enteredpin)
			studentpin=get_object_or_404(Pin,student=request.POST.get('Name'))
			if mainpin == studentpin.pin:
				context={
					"Student":stuff,
					"Result":queryset3,
					'schoollogo': school,
					'letter':letter,
					}
				return render(request,"Result.html", context)
			else:
				messages.error(request, 'Invalid card pin , check your input and try again') 
				context = {
					"students": queryset,
					"class":queryset2
					}
				return render(request, "Students.html", context)
		except:
			messages.error(request, 'Invalid card pin , check your input and try again') 
			context = {
				"students": queryset,
				"class":queryset2
			}
			return render(request, "Students.html", context)
		
		
	

def result_pdf_view(request,Name,Classname):
	stuff=get_object_or_404(Student,Name=Name)
	queryset=Result.objects.filter(Name=Name,Class=Classname)
	school=School.objects.all()
	letter=Newsletter.objects.all()
	template_path ='Result_pdf.html'
	context={
		"Student":stuff,
		"Result":queryset,
		'schoollogo': school,
		'letter':letter,
		}
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment'; filename="Result.pdf"
	template = get_template(template_path)
	html = template.render(context)
	pisa_status = pisa.CreatePDF(
		html, dest=response)
	if pisa_status.err:
		return HttpResponse('We had some errors <pre>' + html + '</pre>')
	return response


	
def activation_view(request):
	context = {
		}
	return render(request, "activation.html", context)
	
	#Activate the Junior Students

def createjuniorstudent1a_view(request):
	student=Excelfiles()
	student.createJuniorStudent1a()
	context = {
		}
	return render(request, "Congratulation.html", context)

def createjuniorstudent1b_view(request):
	student=Excelfiles()
	student.createJuniorStudent1b()
	context = {
		}
	return render(request, "Congratulation.html", context)
def createjuniorstudent1c_view(request):
	student=Excelfiles()
	student.createJuniorStudent1c()
	context = {
		}
	return render(request, "Congratulation.html", context)

def createjuniorstudent2a_view(request):
	student=Excelfiles()
	student.createJuniorStudent2a()
	context = {
		}
	return render(request, "Congratulation.html", context)
def createjuniorstudent2b_view(request):
	student=Excelfiles()
	student.createJuniorStudent2b()
	context = {
		}
	return render(request, "Congratulation.html", context)

def createjuniorstudent3_view(request):
	student=Excelfiles()
	student.createJuniorStudent3()
	context = {
		}
	return render(request, "Congratulation.html", context)

# create Jss1,2 & 3 Result 

def createjuniorresult1a_view(request):
	result=Student()
	result.createJuniorResult1a()
	context = {
		}
	return render(request, "Congratulation.html", context)
def createjuniorresult1b_view(request):
	result=Student()
	result.createJuniorResult1b()
	context = {
		}
	return render(request, "Congratulation.html", context)
def createjuniorresult1c_view(request):
	result=Student()
	result.createJuniorResult1c()
	context = {
		}
	return render(request, "Congratulation.html", context)

def createjuniorresult2a_view(request):
	result=Student()
	result.createJuniorResult2a()
	context = {
		}
	return render(request, "Congratulation.html", context)

def createjuniorresult2b_view(request):
	result=Student()
	result.createJuniorResult2b()
	context = {
		}
	return render(request, "Congratulation.html", context)

def createjuniorresult3_view(request):
	result=Student()
	result.createJuniorResult3()
	context = {
		}
	return render(request, "Congratulation.html", context)

# Activate the Senior Students

def createseniorstudent_view(request):
	student=Excelfiles()
	student.createSeniorStudents()
	context = {
	 }
	return render(request, "Congratulation.html", context)

# Activate the Senior Result
	
def createseniorresult1_view(request):
	result=Student()
	result.createSeniorResult1()
	context = {
		}
	return render(request, "Congratulation.html", context)

def createseniorresult2_view(request):
	result=Student()
	result.createSeniorResult2()
	context = {
		}
	return render(request, "Congratulation.html", context)
	
# Create the Student Pin with the name 

def createPin(request):
	myPin=Pin()
	myPin.generatePin()
	Studentpin=Pin.objects.all()
	context = {
	"pins": Studentpin,
		}
	return render(request, "pins.html", context)
	
