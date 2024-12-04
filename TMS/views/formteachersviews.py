from django.shortcuts import get_object_or_404, render
from SRMS.models import *
from ..models import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
# from CBT.models import *
import json

# ////////////////////////////

# Form teachers View for CRUD Students Details
@login_required
def Students_view(request, Classname, session_id):
    classobject = Class.objects.get(Class=Classname)
    sessionobject = AcademicSession.objects.get(id=session_id)
    sessions = AcademicSession.objects.all()
    # Fetch students enrolled in this class and session
    students = StudentClassEnrollment.objects.filter(
        student_class=classobject, academic_session=sessionobject
    ).select_related("student")  # Use select_related for optimized queries

    context = {
        "class": classobject,
        "session": sessionobject,
        "students": students,
        "sessions":sessions
    }
    return render(request, "students.html", context)


def createstudent_view(request):
    data=json.loads(request.body)
    student_name=data['studentname']
    student_sex=data['Student_sex']
    student_class=data['studentclass']
    academic_session = data.get("academicsession")
    classobject = Class.objects.get(Class=student_class)
    
    try:
        # Fetch or validate class and session objects
        classobject = get_object_or_404(Class, Class=student_class)
        sessionobject = get_object_or_404(AcademicSession, session=academic_session)

        # Fetch or create the student record
        student, created = Students_Pin_and_ID.objects.get_or_create(
            student_name=student_name, Sex=student_sex
        )

        # Fetch or create the enrollment record
        enrollment, _ = StudentClassEnrollment.objects.get_or_create(
            student=student, student_class=classobject, academic_session=sessionobject
        )

        message = (
            f"{student.student_name} record has been {'created' if created else 'updated'} "
            f"successfully in {classobject.Class} for {sessionobject.session}."
        )

        return JsonResponse(
            {
                "student_ID": student.id,
                "student_id": student.student_id,
                "student_name": student.student_name,
                "student_sex": student.Sex,
                "message": message,
            },
            safe=False,
        )

    except Exception as e:
        print(str(e))
        return JsonResponse({"error": f"Something went wrong: {str(e)}"}, safe=False)


def updatestudent_view(request):
    data=json.loads(request.body)
    student_id=data['studentID']
    student_name=data['studentname']
    student_sex=data['Student_sex']
    student_class=data['studentclass']
    academic_session = data["academicsession"]
    # Fetch class and session objects
    classobject = Class.objects.get(Class=student_class)
    sessionobject = AcademicSession.objects.get(session=academic_session)

    try:
        # Update the student record
        updateStudent = Students_Pin_and_ID.objects.get(id=student_id)
        updateStudent.student_name = student_name
        updateStudent.Sex = student_sex
        updateStudent.save()

        # Update or create the enrollment record
        enrollment, created = StudentClassEnrollment.objects.update_or_create(
            student=updateStudent,
            academic_session=sessionobject,
            defaults={"student_class": classobject},
        )

        context = {
            "student_ID": updateStudent.id,
            "student_id": updateStudent.student_id,
            "student_name": updateStudent.student_name,
            "student_sex": updateStudent.Sex,
            "message": f"{updateStudent.student_name}'s record has been updated successfully for {classobject.Class} in {sessionobject.session}.",
        }
        return JsonResponse(context, safe=False)
    except Exception as e:
        return JsonResponse({"error": f"Something went wrong: {str(e)}"}, safe=False)


def DeleteStudents_view(request):
    studentidstodelete=json.loads(request.body)
    studentnamesdeleted=[]   
    try:
        for student_id in studentidstodelete:
            student = Students_Pin_and_ID.objects.get(id=student_id)
            # Delete their enrollment records
            StudentClassEnrollment.objects.filter(student=student).delete()
            studentnamesdeleted.append(student.student_name)
        context={
            'message': f'{studentnamesdeleted} records have been deleted Successfully'
        }
        return JsonResponse(context, safe=False)
    except:
        return JsonResponse({'error': 'something went wrong' }, safe=False)



# Form teachers View for CRUD Students Results
@login_required
def PublishResults_view(request,Classname):
    Terms=Term.objects.all()
    academic_session= AcademicSession.objects.all()
    class_object = Class.objects.get(Class=Classname)
    subjects_allocation = Subjectallocation.objects.filter(classname=class_object).first()
    subject_code = []
    for subobject in subjects_allocation.subjects.all():
        subject_code.append(subobject.subject_code)
    context = {
        'subjects_allocation': subjects_allocation,
        "class": class_object,
        'sub_list':subject_code,
        "Terms":Terms,
        "academic_session":academic_session,
        "sessions":academic_session
        }
    return render(request, 'Publish_Result.html', context)

def getstudentsubjecttotals_view(request):
    data=json.loads(request.body)
    class_object = Class.objects.get(Class=data['studentclass'])
    term_object = Term.objects.get(term=data['selectedTerm'])
    session_object = AcademicSession.objects.get(session=data['selectedAcademicSession'])
    subjects_allocated = Subjectallocation.objects.filter(classname=class_object).first()
    if not subjects_allocated:
        return JsonResponse({"error": "No subjects allocated to this class"}, status=400)
    students = StudentClassEnrollment.objects.filter(
            student_class=class_object,
            academic_session=session_object
        ).select_related("student")
    final_list = []
    # get all the Students related to the Class
    for student in students:
        Resultdetails,_=Student_Result_Data.objects.get_or_create(Student_name=student.student,Term=term_object,Academicsession=session_object)
        student_dict = {
            'id':student.student.id,
            'Name': student.student.student_name,
            'subjects':[],
        }
        for subobject in subjects_allocated.subjects.all():
            subject = {}
            try:
                subresult = Result.objects.get(students_result_summary=Resultdetails, Subject=subobject)
                subject['subject_code'] = subobject.subject_code
                subject['subject_name'] = subobject.subject_name
                subject['Total'] = subresult.Total
                subject['published'] = subresult.published
            except:
                subject['subject_code'] = subobject.subject_code
                subject['subject_name'] = subobject.subject_name
                subject['Total'] = "-"
                subject['published'] = False
            student_dict['subjects'].append(subject)
            student_dict['published'] = Resultdetails.published
        final_list.append(student_dict)
    return JsonResponse(final_list, safe=False)


def publishstudentresult_view(request):
    try:
        data=json.loads(request.body)
        termobject=data['classdata']['selectedTerm']
        Acadsessionobject=data['classdata']['selectedAcademicSession']
        Classdata=data['classdata']['studentclass']
        
        print(data['data'])
        for studentdata in data['data']:
            classobject=Class.objects.get(Class=Classdata)
            resultterm = Term.objects.get(term=termobject)
            resultsession = AcademicSession.objects.get(session=Acadsessionobject)
            studentnumber = StudentClassEnrollment.objects.filter(student_class=classobject,academic_session=resultsession).count()
            student = Students_Pin_and_ID.objects.get(student_name=studentdata['Name'])

            try:
                studentresult=Student_Result_Data.objects.get(Student_name=student,Term=resultterm,Academicsession=resultsession)
                studentresult.TotalScore=studentdata['Total']
                studentresult.Totalnumber= studentnumber
                studentresult.Average=studentdata['Ave']
                studentresult.Position=studentdata['Position']
                studentresult.Remark=studentdata['Remarks']
                studentresult.published = True
                studentresult.save()
            except Exception as e:
                print(str(e))
                continue
        return JsonResponse('Results have been Published and its now open to the Students', safe=False)
    except:
        return JsonResponse({'something went wrong, try again later' }, safe=False)


def unpublish_classresults_view(request):
    data=json.loads(request.body)
    termobject=Term.objects.get(term=data['classdata']['selectedTerm'])
    Acadsessionobject=AcademicSession.objects.get(session=data['classdata']['selectedAcademicSession'])
    
    for student_data in data['data']:
        try:
            student = Students_Pin_and_ID.objects.get(
                    student_name=student_data['Name']
                )
            studentresult=Student_Result_Data.objects.get(Student_name=student,Term=termobject,Academicsession=Acadsessionobject)
            studentresult.published = False
            studentresult.save()
        except:
            continue
    return JsonResponse('Results have been Unpublished and its now closed to the Students', safe=False)


# -----------------------------------------------------------------------------------
# Annual views for the Form teachers
# -----------------------------------------------------------------------------------
@login_required
def PublishAnnualResults_view(request,Classname):
    academic_session= AcademicSession.objects.all()
    class_object = Class.objects.get(Class=Classname)
    subjects_allocation = Subjectallocation.objects.filter(classname=class_object).first()
    subject_code = []
    sessions = AcademicSession.objects.all()
    for subobject in subjects_allocation.subjects.all():
        subject_code.append(subobject.subject_code)
    context = {
        'subjects_allocation': subjects_allocation,
        "class": class_object,
        'sub_list':subject_code,
        "academic_session":academic_session,
        "sessions":sessions
        }
    return render(request, 'Annual_Publish_Result.html', context)


def annual_class_computation_view(request):
    data=json.loads(request.body)
    classobject=Class.objects.get(Class=data['studentclass'])
    Acadsessionobject=AcademicSession.objects.get(session=data['selectedAcademicSession'])
    students = StudentClassEnrollment.objects.filter(
            student_class=classobject,
            academic_session=Acadsessionobject
        ).select_related("student")
    subjects_allocated = Subjectallocation.objects.filter(classname=classobject).first()
    final_list = []
    for student in students:
        studentdict={
            "id": student.student.id,
            'Name':student.student.student_name,
            "subjects":[]
        }
        for subobject in subjects_allocated.subjects.all():
            subject = {}
            try:
                subject_object = Subject.objects.get(subject_code=subobject.subject_code)
                studentAnnual,_ = AnnualStudent.objects.get_or_create(Student_name=student.student, academicsession=Acadsessionobject)
                subjectAnnual = AnnualResult.objects.get(Student_name=studentAnnual, Subject=subject_object)
                subject['subject_code'] = subobject.subject_code
                subject['subject_name'] = subobject.subject_name
                subject['Average'] = subjectAnnual.Average
                subject['published'] = subjectAnnual.published
            except:
                subject['subject_code'] = subobject.subject_code
                subject['subject_name'] = subobject.subject_name
                subject['Average'] = "-"
                subject['published'] = False
            studentdict['subjects'].append(subject)
            studentdict['published'] = studentAnnual.published
        final_list.append(studentdict)
    return JsonResponse(final_list, safe=False)



def publish_annualstudentresult_view(request):
    try:
        data=json.loads(request.body)
        Acadsessionobject=data['classdata']['selectedAcademicSession']
        Classdata=data['classdata']['studentclass']
        for studentdata in data['data']:
            classobject=Class.objects.get(Class=Classdata)
            resultsession = AcademicSession.objects.get(session=Acadsessionobject)
            student = Students_Pin_and_ID.objects.get(student_name=studentdata['Name'])
            studentnumber = StudentClassEnrollment.objects.filter(student_class=classobject,academic_session=resultsession).count()
            try:
                studentresult=AnnualStudent.objects.get(Student_name=student,academicsession=resultsession)
                studentresult.TotalScore=studentdata['Total']
                studentresult.Totalnumber= studentnumber
                studentresult.Average=studentdata['Average']
                studentresult.Position=studentdata['Position']
                studentresult.Remark=studentdata['Remarks']
                studentresult.Verdict = studentdata['Verdict']
                studentresult.published = True
                studentresult.save()
            except Exception as e:
                print(str(e))
                continue
        return JsonResponse('Results have been Published and its now open to the Students', safe=False)
    except:
        return JsonResponse({'something went wrong, try again later' }, safe=False)
    

def unpublish_annual_classresults_view(request):
    data=json.loads(request.body)
    classobject=Class.objects.get(Class=data['classdata']['studentclass'])
    Acadsessionobject=AcademicSession.objects.get(session=data['classdata']['selectedAcademicSession'])
    students = StudentClassEnrollment.objects.filter(student_class=classobject,academic_session=Acadsessionobject)
    for student in students:
        try:
            studentresult=AnnualStudent.objects.get(Student_name=student,academicsession=Acadsessionobject)
            studentresult.published = False
            studentresult.save()
        except:
            continue
    return JsonResponse('Results have been Unpublished and its now closed to the Students', safe=False)
