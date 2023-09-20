from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from home.models import School
from django.contrib.auth.decorators import login_required
import base64
base64.encodestring = base64.encodebytes
base64.decodestring = base64.decodebytes
from django.http import HttpResponse
from django.contrib import messages
from django.http import JsonResponse

def get_Students(request, Classname):
    Students = Students_Pin_and_ID.objects.filter(student_class=Classname)
    Students_list = list(Students.values('id', 'student_name'))
    return JsonResponse(Students_list, safe=False)


def classes_view(request):
	queryset= Class.objects.all()
	if request.method == 'POST':
	# get the Student name from the inque
		student_name=str(request.POST['student_name'])
		student_id=str(request.POST['student_id'])
		Pin=str(request.POST['student_pin'])
		# Get the Student details, the Students_Result_Details and the Results (Both Annual & Termly )
		try:
			student = Students_Pin_and_ID.objects.get(student_name=student_name,student_id=student_id,student_pin=Pin)
			if Student.objects.filter(student_name=student_name,Student_id=student_id).exists():
				Student_Result_details=Student.objects.get(student_name=student_name,Student_id=student_id)
				Student_Results=Result.objects.filter(student_name=student_name,Student_id=student_id)

				# for Newsletter ///
				is_term_newsletter = False
				term_newsletter = None
				# endeavour to change the Hard Coding "3rd Term" later to str(Student_Result_details.Term)
				if Newsletter.objects.filter(Term = "3rd Term").exists():
					is_term_newsletter=True
					term_newsletter=Newsletter.objects.get(Term="3rd Term")

				labels = []
				data = []
				for result in Student_Results:
					labels.append(result.Subject)
					data.append(result.Total)					
				if AnnualStudent.objects.filter(student_name=student_name,Student_id=student_id).exists():
					Annual_Result=True
					Annual_Student_Result_details=AnnualStudent.objects.get(student_name=student_name,Student_id=student_id)
					Annual_Student_Results=AnnualResult.objects.filter(student_name=student_name,Student_id=student_id)
					PromotionVerdict=int(float(Annual_Student_Result_details.Average))
					context={
						"student_details":student,
						"Result_details":Student_Result_details,
						"Results":Student_Results,
						"labels":labels,
						"data":data,
						"AnnualStudent":Annual_Student_Result_details,
						'AnnualResult': Annual_Student_Results,
						"Annual_Result":Annual_Result,
						"PromotionVerdict":PromotionVerdict,
						"isTermNewsletter":is_term_newsletter,
						"TermNewsletter":term_newsletter
						}
					return render(request,"Result.html", context)
				else:
					Annual_Result=False
					context={
						"Annual_Result":Annual_Result,
						"student_details":student,
						"Result_details":Student_Result_details,
						"Results":Student_Results,
						"labels":labels,
						"data":data,
						"PromotionVerdict":PromotionVerdict,
						"isTermNewsletter":is_term_newsletter,
						"TermNewsletter":term_newsletter
								}
					return render(request,"Result.html", context)
			else:
				return render(request,"404.html")

		except Students_Pin_and_ID.DoesNotExist:
			# Display an error message if the student does not exist
			classes=Class.objects.all()
			context={
				"classes":classes,
			}
			messages.error(request, 'Check your Student id or the Pin and try again , make sure you are entering it Correctly')
			return render(request, "Classes.html",context)
	else:
		context={
			"classes": queryset,
		}
		return render(request, "Classes.html",context)

# Result Activation Code /////////////////////////////////////

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
	result.createSeniorAnnual2b()
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

