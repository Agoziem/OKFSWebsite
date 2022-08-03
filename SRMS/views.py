from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
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
	
def students_view(request,Classname,id):
	queryset=Student.objects.filter(Class=Classname)
	queryset3=Assignments.objects.filter(Class=id)
	queryset2=Class.objects.get(Class=Classname)
	context = {
		"students": queryset,
		"class":queryset2,
		"Assignments":queryset3,
    }
	return render(request, "Students.html", context)
	
def result_view(request,Classname):
	stu=str(request.POST.get('Name'))
	studentname=stu.upper().strip()
	queryset1=Student.objects.filter(Class=Classname)
	# queryset2=AnnualStudent.objects.filter(Class=Classname)
	queryset3=Class.objects.get(Class=Classname)
	stuff1=get_object_or_404(Student,Name=studentname)
	stuff2=get_object_or_404(AnnualStudent,Name=studentname)
	queryset4=Result.objects.filter(Name=studentname,Class=Classname)
	queryset5=AnnualResult.objects.filter(Name=studentname,Class=Classname)
	letter=Newsletter.objects.all()
	school=School.objects.all()
	if request.method=='POST':
		try:
			enteredpin=request.POST.get('Pin')
			mainpin=int(enteredpin)
			studentpin=get_object_or_404(Pin,student=studentname)
			if mainpin == studentpin.pin:
				context={
					"Student":stuff1,
					"AnnualStudent":stuff2,
					"Result":queryset4,
					'AnnualResult': queryset5,
					'schoollogo': school,
					'letter':letter,
					}
				return render(request,"Result.html", context)
			else:
				messages.error(request, 'Invalid card pin , check your input and try again') 
				context = {
					"students": queryset1,
					"class":queryset3
					}
				return render(request, "Students.html", context)
		except:
			messages.error(request, 'Invalid card pin , check your input and try again') 
			context = {
				"students": queryset1,
				"class":queryset3
			}
			return render(request, "Students.html", context)
		
		
	

def result_pdf_view(request,Name,Classname):
	stuff=get_object_or_404(Student,Name=Name)
	stuff2=get_object_or_404(AnnualStudent,Name=Name)
	queryset4=Result.objects.filter(Name=Name,Class=Classname)
	queryset5=AnnualResult.objects.filter(Name=Name,Class=Classname)
	school=School.objects.all()
	letter=Newsletter.objects.all()
	template_path ='Result_pdf.html'
	context={
		"AnnualStudent":stuff2,
		"Student":stuff,
		"Result":queryset4,
		'schoollogo': school,
		'letter':letter,
		'AnnualResult': queryset5,
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
	

def createPin(request):
	myPin=Pin()
	myPin.generatePin()
	Studentpin=Pin.objects.all()
	context = {
	"pins": Studentpin,
		}
	return render(request, "pins.html", context)

# Create Junior Students Termly Results Details

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

# create Junior Students Termly Results

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


# Create Junior Student's Annual Details

def createjuniorstudentAnnual1a_view(request):
	student=Excelfiles()
	student.createJuniorStudentAnnual1a()
	context = {
		}
	return render(request, "Congratulation.html", context)

def createjuniorstudentAnnual1b_view(request):
	student=Excelfiles()
	student.createJuniorStudentAnnual1b()
	context = {
		}
	return render(request, "Congratulation.html", context)
def createjuniorstudentAnnual1c_view(request):
	student=Excelfiles()
	student.createJuniorStudentAnnual1c()
	context = {
		}
	return render(request, "Congratulation.html", context)

def createjuniorstudentAnnual2a_view(request):
	student=Excelfiles()
	student.createJuniorStudentAnnual2a()
	context = {
		}
	return render(request, "Congratulation.html", context)
def createjuniorstudentAnnual2b_view(request):
	student=Excelfiles()
	student.createJuniorStudentAnnual2b()
	context = {
		}
	return render(request, "Congratulation.html", context)

def createjuniorstudentAnnual3_view(request):
	student=Excelfiles()
	student.createJuniorStudentAnnual3()
	context = {
		}
	return render(request, "Congratulation.html", context)

# create Junior Annual Results

def createjuniorresultAnnual1a_view(request):
	result=AnnualStudent()
	result.createJuniorAnnual1a()
	context = {
		}
	return render(request, "Congratulation.html", context)

def createjuniorresultAnnual1b_view(request):
	result=AnnualStudent()
	result.createJuniorAnnual1b()
	context = {
		}
	return render(request, "Congratulation.html", context)
def createjuniorresultAnnual1c_view(request):
	result=AnnualStudent()
	result.createJuniorAnnual1c()
	context = {
		}
	return render(request, "Congratulation.html", context)

def createjuniorresultAnnual2a_view(request):
	result=AnnualStudent()
	result.createJuniorAnnual2a()
	context = {
		}
	return render(request, "Congratulation.html", context)

def createjuniorresultAnnual2b_view(request):
	result=AnnualStudent()
	result.createJuniorAnnual2b()
	context = {
		}
	return render(request, "Congratulation.html", context)

def createjuniorresultAnnual3_view(request):
	result=AnnualStudent()
	result.createJuniorAnnual3()
	context = {
		}
	return render(request, "Congratulation.html", context)



# Termly Senior Students details

def createseniorstudent_view(request):
	student=Excelfiles()
	student.createSeniorStudents()
	context = {
	 }
	return render(request, "Congratulation.html", context)

# Termly Senior Students Result
	
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
	
# Annual Senior Students Result  

def createseniorstudentAnnual_view(request):
	student=Excelfiles()
	student.createSeniorStudentsAnnual()
	context = {
	 }
	return render(request, "Congratulation.html", context)

# Activate the Senior Result
	
def createseniorresultAnnual1_view(request):
	result=AnnualStudent()
	result.createSeniorAnnual1()
	context = {
		}
	return render(request, "Congratulation.html", context)

def createseniorresultAnnual2_view(request):
	result=AnnualStudent()
	result.createSeniorAnnual2()
	context = {
		}
	return render(request, "Congratulation.html", context)

	
