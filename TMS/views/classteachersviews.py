from django.shortcuts import render
from SRMS.models import *
from ..models import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
# from CBT.models import *
import json

@login_required
def result_computation_view(request,Classname,id):
    teacher = Teacher.objects.get(id=id)
    Terms=Term.objects.all()
    academic_session= AcademicSession.objects.all()
    classobject = Class.objects.get(Class=Classname)
    subjectsforclass=Subjectallocation.objects.get(classname=classobject)
    subjects_taught_for_class = teacher.subjects_taught.filter(id__in=subjectsforclass.subjects.values_list('id', flat=True))
    context={
        'class':classobject,
        "Terms":Terms,
        "academic_session":academic_session,
        "subjects_taught_for_class":subjects_taught_for_class,
        "sessions":academic_session
        } 
    return render(request,'Result_computation.html',context)

@login_required
def get_students_result_view(request):
    data=json.loads(request.body)
    studentResults = []
    try:
        classobject = Class.objects.get(Class=data['studentclass'])
        subjectobject = Subject.objects.get(subject_name=data['studentsubject'])
        term=Term.objects.get(term=data['selectedTerm'])
        session=AcademicSession.objects.get(session=data['selectedAcademicSession'])
        students = StudentClassEnrollment.objects.filter(student_class=classobject,academic_session=session)
        
        for studentresult in students:
            student_result_details,created = Student_Result_Data.objects.get_or_create(Student_name=studentresult.student,Term=term,Academicsession=session)
            student_result_object, created = Result.objects.get_or_create(Subject=subjectobject, students_result_summary=student_result_details)
            studentResults.append({
                'Name': student_result_object.students_result_summary.Student_name.student_name,
                '1sttest': student_result_object.FirstTest,
                '1stAss': student_result_object.FirstAss,
                'Project': student_result_object.Project,
                'MidTermTest': student_result_object.MidTermTest,
                '2ndTest': student_result_object.SecondAss,
                '2ndAss': student_result_object.SecondTest,
                'Exam': student_result_object.Exam,
                "studentID":student_result_object.students_result_summary.Student_name.student_id,
                'published': student_result_object.published,
            })
        return JsonResponse(studentResults, safe=False)
    except:
        return JsonResponse(studentResults, safe=False)

@login_required
def update_student_result_view(request):
    data=json.loads(request.body)
    subject=data['classdata']['studentsubject']
    Classdata=data['classdata']['studentclass']
    student=data['formDataObject']['Name']
    studentID=data['formDataObject']['studentID']
    # classobject= Class.objects.get(Class=Classdata)
    term=Term.objects.get(term=data['classdata']['selectedTerm'])
    session=AcademicSession.objects.get(session=data['classdata']['selectedAcademicSession'])
    studentobject= Students_Pin_and_ID.objects.get(student_id=studentID,student_name=student)
    subjectobject = Subject.objects.get(subject_name=subject)
    student_result_details = Student_Result_Data.objects.get(Student_name=studentobject,Term=term,Academicsession=session)
    studentResult = Result.objects.get(students_result_summary=student_result_details, Subject=subjectobject)
    studentResult.FirstTest  = data['formDataObject']['1sttest']
    studentResult.FirstAss  = data['formDataObject']['1stAss']
    studentResult.Project  = data['formDataObject']['Project']
    studentResult.MidTermTest  = data['formDataObject']['MidTermTest']
    studentResult.SecondAss = data['formDataObject']['2ndAss']
    studentResult.SecondTest = data['formDataObject']['2ndTest']
    studentResult.Exam = data['formDataObject']['Exam']
    studentResult.save()

    return JsonResponse('Result Updated Successfully', safe=False)
    

def submitallstudentresult_view(request):
    data=json.loads(request.body)
    subject=data['classdata']['studentsubject']
    Classdata=data['classdata']['studentclass']
    term=Term.objects.get(term=data['classdata']['selectedTerm'])
    session=AcademicSession.objects.get(session=data['classdata']['selectedAcademicSession'])
    for result in data['data']:
        # classobject= Class.objects.get(Class=Classdata)
        subjectobject = Subject.objects.get(subject_name=subject)
        studentobject= Students_Pin_and_ID.objects.get(student_id=result['studentID'],student_name=result['Name'])
        student_result_details = Student_Result_Data.objects.get(Student_name=studentobject,Term=term,Academicsession=session)
        studentResult = Result.objects.get(students_result_summary=student_result_details, Subject=subjectobject)
        studentResult.FirstTest=result['1sttest']
        studentResult.FirstAss=result['1stAss']
        studentResult.Project=result['Project']
        studentResult.MidTermTest=result['MidTermTest']
        studentResult.SecondAss=result['2ndTest']
        studentResult.SecondTest=result['2ndAss']
        studentResult.CA=result['CA']
        studentResult.Exam=result['Exam']
        studentResult.Total=result['Total']
        studentResult.Grade=result['Grade']
        studentResult.SubjectPosition=result['Position']
        studentResult.Remark=result['Remarks']
        studentResult.published=True
        studentResult.save()
    return JsonResponse('Results submitted Successfully', safe=False)


def unpublish_results_view(request):
    data=json.loads(request.body)
    subjectobject=data['classdata']['studentsubject']
    termobject=data['classdata']['selectedTerm']
    Acadsessionobject=AcademicSession.objects.get(session=data['classdata']['selectedAcademicSession'])
    Classdata=data['classdata']['studentclass']
    for studentdata in data['data']:
        # classobject=Class.objects.get(Class=Classdata)
        resultterm = Term.objects.get(term=termobject)
        resultsession = AcademicSession.objects.get(session=Acadsessionobject)
        subjectobject = Subject.objects.get(subject_name=subjectobject)
        student = Students_Pin_and_ID.objects.get(student_name=studentdata['Name'],student_id=studentdata['studentID'])
        try:
            student_result_details=Student_Result_Data.objects.get(Student_name=student,Term=resultterm,Academicsession=resultsession)
            studentResult = Result.objects.get(students_result_summary=student_result_details, Subject=subjectobject)
            studentResult.published = False
            studentResult.save()
        except Exception as e:
            print(str(e))
            continue
    return JsonResponse('Results have been unpublished and its no longer opened to the Students', safe=False)


# ---------------------------------
# Annual Result Computation Views
# ---------------------------------
def annualresult_computation(request,Classname,id):
    teacher = Teacher.objects.get(id=id)
    academic_session= AcademicSession.objects.all()
    classobject = Class.objects.get(Class=Classname)
    subjectsforclass=Subjectallocation.objects.get(classname=classobject)
    subjects_taught_for_class = teacher.subjects_taught.filter(id__in=subjectsforclass.subjects.values_list('id', flat=True))
    context={
        'class':classobject,
        "academic_session":academic_session,
        "subjects_taught_for_class":subjects_taught_for_class,
        "sessions":academic_session
        } 
    return render(request,'Annual_Results.html',context)

def annual_result_computation_view(request):
    data = json.loads(request.body)
    subject_name = data['studentsubject']
    class_name = data['studentclass']
    academic_session = data['selectedAcademicSession']
    class_object = Class.objects.get(Class=class_name)
    session = AcademicSession.objects.get(session=academic_session)
    subject_object = Subject.objects.get(subject_name=subject_name)
    students = StudentClassEnrollment.objects.filter(student_class=class_object,academic_session=session)
    terms = Term.objects.all()
    students_annuals = []

    for student in students:
        studentAnnual,created = AnnualStudent.objects.get_or_create(Student_name=student, academicsession=session)
        student_annual_details, created = AnnualResult.objects.get_or_create(Student_name=studentAnnual, Subject=subject_object)
        student_annual_details.Total = 0  # Ensure Total is initialized to zero
        termsobject = {}  # Reset for each student
        for term in terms:
            try:
                student_result_details, created = Student_Result_Data.objects.get_or_create(Student_name=student, Term=term, Academicsession=session)
                student_result, created = Result.objects.get_or_create(students_result_summary=student_result_details, Subject=subject_object)
                termsobject[term.term] = student_result.Total
            except (Student_Result_Data.DoesNotExist, Result.DoesNotExist):
                continue
            except Exception as e:
                print(str(e))
                continue
        try:
            students_annuals.append({
                "studentID": student.student_id,
                'Name': student.student_name,
                'terms': termsobject,
                'published': student_annual_details.published
            })
        except Exception as e:
            print(str(e))
            continue
    
    return JsonResponse(students_annuals, safe=False)


def publish_annual_results(request):
    data = json.loads(request.body)
    subject_name = data['classdata']['studentsubject']
    class_name = data['classdata']['studentclass']
    academic_session = data['classdata']['selectedAcademicSession']
    class_object = Class.objects.get(Class=class_name)
    session = AcademicSession.objects.get(session=academic_session)
    subject_object = Subject.objects.get(subject_name=subject_name)
    for result in data['data']:
        student = Students_Pin_and_ID.objects.get(student_id=result['studentID'], student_name=result['Name'])
        studentAnnual = AnnualStudent.objects.get(Student_name=student, academicsession=session)
        student_annual_details = AnnualResult.objects.get(Student_name=studentAnnual, Subject=subject_object)
        student_annual_details.FirstTermTotal = result["terms"]["1st Term"]
        student_annual_details.SecondTermTotal = result["terms"]["2nd Term"]
        student_annual_details.ThirdTermTotal = result["terms"]["3rd Term"]
        student_annual_details.Total = result['Total']
        student_annual_details.Average = result['Average']
        student_annual_details.Grade = result['Grade']
        student_annual_details.SubjectPosition = result['Position']
        student_annual_details.Remark = result['Remarks']
        student_annual_details.published = True
        student_annual_details.save()
    return JsonResponse('Results have been published', safe=False)


def unpublish_annual_results(request):
    data = json.loads(request.body)
    subject_name = data['classdata']['studentsubject']
    class_name = data['classdata']['studentclass']
    academic_session = data['classdata']['selectedAcademicSession']
    class_object = Class.objects.get(Class=class_name)
    session = AcademicSession.objects.get(session=academic_session)
    subject_object = Subject.objects.get(subject_name=subject_name)
    for studentdata in data['data']:
        student = Students_Pin_and_ID.objects.get(student_name=studentdata['Name'])
        studentAnnual = AnnualStudent.objects.get(Student_name=student, academicsession=session)
        student_annual_details = AnnualResult.objects.get(Student_name=studentAnnual, Subject=subject_object)
        student_annual_details.published = False
        student_annual_details.save()
    return JsonResponse('Results have been unpublished', safe=False)
    
    




	
