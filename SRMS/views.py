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
	# studentname=stu.upper().strip()

	queryset3=Class.objects.get(Class=Classname)

	queryset1=Student.objects.filter(Class=Classname)	
	stuff1=Student.objects.get(Name=stu,Class=Classname)
	queryset4=Result.objects.filter(Name=stu,Class=Classname)

	# queryset2=AnnualStudent.objects.filter(Class=Classname)
	# stuff2=get_object_or_404(AnnualStudent,Name=studentname)
	# queryset5=AnnualResult.objects.filter(Name=studentname,Class=Classname)
	
	
	letter=Newsletter.objects.all()
	school=School.objects.all()
	if request.method=='POST':
		try:
			enteredpin=request.POST.get('Pin')
			mainpin=int(enteredpin)
			studentpin=get_object_or_404(Students_Pin_and_ID,student_name=stu)
			if mainpin == studentpin.student_pin:
				context={
					"Student":stuff1,
					# "AnnualStudent":stuff2,
					"Result":queryset4,
					# 'AnnualResult': queryset5,
					'schoollogo': school,
					'letter':letter,
					}
				return render(request,"Result.html", context)
			else:
				messages.error(request, 'Invalid card pin , check your input and try again or text your "name","class","the Pin on the Card" & "okfs" to 08080982606 to recieve your correct pin') 
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
	# stuff2=get_object_or_404(AnnualStudent,Name=Name)
	queryset4=Result.objects.filter(Name=Name,Class=Classname)
	# queryset5=AnnualResult.objects.filter(Name=Name,Class=Classname)
	school=School.objects.all()
	letter=Newsletter.objects.all()
	template_path ='Result_pdf.html'
	context={
		# "AnnualStudent":stuff2,
		"Student":stuff,
		"Result":queryset4,
		'schoollogo': school,
		'letter':letter,
		# 'AnnualResult': queryset5,
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
	student=Excelfiles()
	student.readPin()
	context = {
		}
	return render(request, "pins.html", context)


# TERMLY

# Students Termly Data View /////////////////////////////
# Jss1 /////////////////////////////////////////
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
# Jss2 /////////////////////////////////////////
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
def createjuniorstudent2c_view(request):
	student=Excelfiles()
	student.createJuniorStudent2c()
	context = {
		}
	return render(request, "Congratulation.html", context)

# Jss3 //////////////////////////////////////////////
def createjuniorstudent3a_view(request):
	student=Excelfiles()
	student.createJuniorStudent3a()
	context = {
		}
	return render(request, "Congratulation.html", context)
def createjuniorstudent3b_view(request):
	student=Excelfiles()
	student.createJuniorStudent3b()
	context = {
		}
	return render(request, "Congratulation.html", context)

# Ss1 ////////////////////////////////////////////////
def createseniorstudent1_view(request):
	student=Excelfiles()
	student.createSeniorStudents1()
	context = {
	 }
	return render(request, "Congratulation.html", context)
# SS2 ////////////////////////////////////////////////
def createseniorstudent2_view(request):
	student=Excelfiles()
	student.createSeniorStudents2()
	context = {
	 }
	return render(request, "Congratulation.html", context)
# SS3 ///////////////////////////////////////////////
def createseniorstudent3_view(request):
	student=Excelfiles()
	student.createSeniorStudents3()
	context = {
	 }
	return render(request, "Congratulation.html", context)


# Students Termly Results View /////////////////////////////////////

# Jss1 //////////////////////////////////
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

# Jss2 /////////////////////////////////////////
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
def createjuniorresult2c_view(request):
	result=Student()
	result.createJuniorResult2c()
	context = {
		}
	return render(request, "Congratulation.html", context)

# Jss3 ////////////////////////////////////
def createjuniorresult3a_view(request):
	result=Student()
	result.createJuniorResult3a()
	context = {
		}
	return render(request, "Congratulation.html", context)
def createjuniorresult3b_view(request):
	result=Student()
	result.createJuniorResult3b()
	context = {
		}
	return render(request, "Congratulation.html", context)

# SS1 ////////////////////////////////////////	
def createseniorresult1_view(request):
	result=Student()
	result.createSeniorResult1()
	context = {
		}
	return render(request, "Congratulation.html", context)
# SS2 ////////////////////////////////////////	
def createseniorresult2a_view(request):
	result=Student()
	result.createSeniorResult2a()
	context = {
		}
	return render(request, "Congratulation.html", context)
def createseniorresult2b_view(request):
	result=Student()
	result.createSeniorResult2b()
	context = {
		}
	return render(request, "Congratulation.html", context)
# SS3 ////////////////////////////////////////	
def createseniorresult3a_view(request):
	result=Student()
	result.createSeniorResult3a()
	context = {
		}
	return render(request, "Congratulation.html", context)
def createseniorresult3b_view(request):
	result=Student()
	result.createSeniorResult3b()
	context = {
		}
	return render(request, "Congratulation.html", context)


# ANNUAL 

# Students Annual Details Views /////////////////////////////////////

# Jss1 /////////////////////////////////////////
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
# Jss2 /////////////////////////////////////////
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
def createjuniorstudentAnnual2c_view(request):
	student=Excelfiles()
	student.createJuniorStudentAnnual2c()
	context = {
		}
	return render(request, "Congratulation.html", context)
# Jss3 /////////////////////////////////////////
def createjuniorstudentAnnual3a_view(request):
	student=Excelfiles()
	student.createJuniorStudentAnnual3a()
	context = {
		}
	return render(request, "Congratulation.html", context)
def createjuniorstudentAnnual3b_view(request):
	student=Excelfiles()
	student.createJuniorStudentAnnual3b()
	context = {
		}
	return render(request, "Congratulation.html", context)
# SS1 /////////////////////////////////////////
def createseniorstudentAnnual1_view(request):
	student=Excelfiles()
	student.createSeniorStudentsAnnual1()
	context = {
	 }
	return render(request, "Congratulation.html", context)
# SS2 ///////////////////////////////////////////
def createseniorstudentAnnual2_view(request):
	student=Excelfiles()
	student.createSeniorStudentsAnnual2()
	context = {
	 }
	return render(request, "Congratulation.html", context)
# SS3 ///////////////////////////////////////////
def createseniorstudentAnnual3_view(request):
	student=Excelfiles()
	student.createSeniorStudentsAnnual3()
	context = {
	 }
	return render(request, "Congratulation.html", context)





#  Students Annual Results /////////////////////////////////////////////////

# Jss1 ////////////////////////////////////////
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

# Jss2 ////////////////////////////////////////
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
def createjuniorresultAnnual2c_view(request):
	result=AnnualStudent()
	result.createJuniorAnnual2c()
	context = {
		}
	return render(request, "Congratulation.html", context)

# Jss3 ////////////////////////////////////////
def createjuniorresultAnnual3a_view(request):
	result=AnnualStudent()
	result.createJuniorAnnual3a()
	context = {
		}
	return render(request, "Congratulation.html", context)
def createjuniorresultAnnual3b_view(request):
	result=AnnualStudent()
	result.createJuniorAnnual3b()
	context = {
		}
	return render(request, "Congratulation.html", context)

# SS1 ////////////////////////////////////////
def createseniorresultAnnual1_view(request):
	result=AnnualStudent()
	result.createSeniorAnnual1()
	context = {
		}
	return render(request, "Congratulation.html", context)

# SS2 /////////////////////////////////////////
def createseniorresultAnnual2a_view(request):
	result=AnnualStudent()
	result.createSeniorAnnual2a()
	context = {
		}
	return render(request, "Congratulation.html", context)
def createseniorresultAnnual2b_view(request):
	result=AnnualStudent()
	result.createSeniorAnnual2a()
	context = {
		}
	return render(request, "Congratulation.html", context)
# SS3 /////////////////////////////////////////
def createseniorresultAnnual3a_view(request):
	result=AnnualStudent()
	result.createSeniorAnnual3a()
	context = {
		}
	return render(request, "Congratulation.html", context)
def createseniorresultAnnual3b_view(request):
	result=AnnualStudent()
	result.createSeniorAnnual3b()
	context = {
		}
	return render(request, "Congratulation.html", context)

