from django.shortcuts import render
from SRMS.models import *
from ..models import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
# from CBT.models import *
import json

# ////////////////////////////

# Form teachers View for CRUD Students Details
@login_required
def Students_view(request,Classname):
    classobject = Class.objects.get(Class=Classname)
    students = Students_Pin_and_ID.objects.filter(student_class=classobject)
    context={
        'class':classobject,
        "students":students
        } 
    return render(request,'students.html',context)

def createstudent_view(request):
    data=json.loads(request.body)
    student_name=data['studentname']
    student_sex=data['Student_sex']
    student_class=data['studentclass']
    classobject = Class.objects.get(Class=student_class)
    try:
        newStudent = Students_Pin_and_ID.objects.create(student_name=student_name,Sex=student_sex,student_class=classobject)
        context={
            'student_ID': newStudent.id, 
            'student_id': newStudent.student_id, 
            'student_name':newStudent.student_name,
            'student_sex':newStudent.Sex,
            'message': f'{newStudent.student_name} record have been created Successfully'
        }
        return JsonResponse(context, safe=False)
    except:
        return JsonResponse({'error': 'something went wrong' }, safe=False)
    
def updatestudent_view(request):
    data=json.loads(request.body)
    student_id=data['studentID']
    student_name=data['studentname']
    student_sex=data['Student_sex']
    student_class=data['studentclass']
    classobject = Class.objects.get(Class=student_class)
    try:
        updateStudent = Students_Pin_and_ID.objects.get(id=student_id)
        updateStudent.student_name=student_name
        updateStudent.Sex= student_sex
        updateStudent.student_class=classobject
        updateStudent.save()
        context={
            'student_ID': updateStudent.id, 
            'student_id': updateStudent.student_id, 
            'student_name':updateStudent.student_name,
            'student_sex':updateStudent.Sex,
            'message': f'{updateStudent.student_name} record have been updated Successfully'
        }
        return JsonResponse(context, safe=False)
    except:
        return JsonResponse({'error': 'something went wrong' }, safe=False)

def DeleteStudents_view(request):
    studentidstodelete=json.loads(request.body)
    studentnamesdeleted=[]   
    try:
        for id in studentidstodelete:
            student = Students_Pin_and_ID.objects.get(id=id)
            studentnamesdeleted.append(student.student_name)
            student.delete()
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
        "academic_session":academic_session
        }
    return render(request, 'Publish_Result.html', context)

def getstudentsubjecttotals_view(request):
    data=json.loads(request.body)
    class_object = Class.objects.get(Class=data['studentclass'])
    term_object = Term.objects.get(term=data['selectedTerm'])
    session_object = AcademicSession.objects.get(session=data['selectedAcademicSession'])
    subjects_allocated = Subjectallocation.objects.filter(classname=class_object).first()
    students = Students_Pin_and_ID.objects.filter(student_class=class_object)
    final_list = []
    # get all the Students related to the Class
    for student in students:
        Resultdetails=Student_Result_Data.objects.filter(Student_name=student,Term=term_object,Academicsession=session_object).first()
        student_dict = {
            'Name': student.student_name,
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
            student_dict[subobject.subject_code] = subject
            student_dict['published'] = Resultdetails.published
        final_list.append(student_dict)
    return JsonResponse(final_list, safe=False)

def publishstudentresult_view(request):
    try:
        data=json.loads(request.body)
        termobject=data['classdata']['selectedTerm']
        Acadsessionobject=data['classdata']['selectedAcademicSession']
        Classdata=data['classdata']['studentclass']
        for studentdata in data['data']:
            classobject=Class.objects.get(Class=Classdata)
            resultterm = Term.objects.get(term=termobject)
            resultsession = AcademicSession.objects.get(session=Acadsessionobject)
            student = Students_Pin_and_ID.objects.get(student_name=studentdata['Name'],student_class=classobject)
            studentnumber=Students_Pin_and_ID.objects.filter(student_class=classobject).count()
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
    classobject=Class.objects.get(Class=data['classdata']['studentclass'])
    termobject=Term.objects.get(term=data['classdata']['selectedTerm'])
    Acadsessionobject=AcademicSession.objects.get(session=data['classdata']['selectedAcademicSession'])
    students = Students_Pin_and_ID.objects.filter(student_class=classobject)
    for student in students:
        try:
            studentresult=Student_Result_Data.objects.get(Student_name=student,Term=termobject,Academicsession=Acadsessionobject)
            studentresult.published = False
            studentresult.save()
        except:
            continue
    return JsonResponse('Results have been Unpublished and its now closed to the Students', safe=False)





	
