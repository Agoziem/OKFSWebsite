from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.contrib.auth.decorators import login_required
import base64
base64.encodestring = base64.encodebytes
base64.decodestring = base64.decodebytes
from django.http import HttpResponse
from django.contrib import messages
from django.http import JsonResponse


def get_Students(request, Classname, session_id):
    sessionobject = AcademicSession.objects.get(id=session_id)
    classobject = Class.objects.get(Class=Classname)
    Studentsenrolled = StudentClassEnrollment.objects.filter(
        student_class=classobject, academic_session=sessionobject
    )
    Students = [enrolled.student for enrolled in Studentsenrolled]
    Students_list = [{'id': student.id, 'student_name': student.student_name} for student in Students]
    return JsonResponse(Students_list, safe=False)


def classes_view(request):
	queryset= Class.objects.all()
	Terms=Term.objects.all()
	academicsession= AcademicSession.objects.all()
	if request.method == 'POST':
	# get the Student name from the inque
		student_name=request.POST['student_name']
		student_id=request.POST['student_id']
		Pin= int(request.POST['student_pin'])
		term = request.POST['Term']
		academic_session = request.POST['AcademicSession']
		# Get the Student details, the Students_Result_Details and the Results (Both Annual & Termly )
		try:
			resultTerm=Term.objects.get(term=term)
			resultSession= AcademicSession.objects.get(id=academic_session)
			studentClass=Class.objects.get(Class=request.POST['student_class'])
			student = Students_Pin_and_ID.objects.get(student_name=student_name,student_id=student_id,student_pin=Pin)
			if Student_Result_Data.objects.filter(Student_name=student,Term=resultTerm,Academicsession=resultSession,published=True).exists():
				Student_Result_details=Student_Result_Data.objects.filter(Student_name=student,Term=resultTerm,Academicsession=resultSession,published=True).first()
				Student_Results=Result.objects.filter(students_result_summary=Student_Result_details,published=True)

				# for Newsletter ///
				is_term_newsletter = False
				term_newsletter = None
				# endeavour to change the Hard Coding "3rd Term" later to str(Student_Result_details.Term)
				if Newsletter.objects.filter(Term = resultTerm).exists():
					is_term_newsletter=True
					term_newsletter=Newsletter.objects.get(Term=resultTerm)

				labels = []
				data = []
				for result in Student_Results:
					labels.append(result.Subject)
					data.append(result.Total)					
				if AnnualStudent.objects.filter(Student_name=student,published=True).exists() and resultTerm.term == "3rd Term":
					Annual_Result=True
					Annual_Student_Result_details=AnnualStudent.objects.get(Student_name=student,academicsession=resultSession,published=True)
					Annual_Student_Results=AnnualResult.objects.filter(Student_name=Annual_Student_Result_details,published=True)
					context={
						"student_details":student,
						"Result_details":Student_Result_details,
						"Results":Student_Results,
						"studentClass":studentClass,
						"labels":labels,
						"data":data,
						"AnnualStudent":Annual_Student_Result_details,
						'AnnualResult': Annual_Student_Results,
						"Annual_Result":Annual_Result,
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
						"studentClass":studentClass,
						"labels":labels,
						"data":data,
						"isTermNewsletter":is_term_newsletter,
						"TermNewsletter":term_newsletter
								}
					return render(request,"Result.html", context)
			else:
				return render(request,"404_page.html")
		except Students_Pin_and_ID.DoesNotExist:
			# Display an error message if the student does not exist
			context={
				"classes": queryset,
				"Terms":Terms,
				"academic_session":academicsession
			}
			messages.error(request, 'Check your Student id or the Pin and try again , make sure you are entering it Correctly')
			return render(request, "Classes.html",context)
	
	context={
		"classes": queryset,
		"Terms":Terms,
		"academic_session":academicsession
	}
	return render(request, "Classes.html",context)



	

