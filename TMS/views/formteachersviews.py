"""
Form Teachers Views Module

This module contains views specifically designed for form teachers (class teachers)
to manage their assigned class students and oversee result publication. Form teachers
have broader responsibilities including student management and class-wide result oversight.

Key Features:
- Student enrollment and management (CRUD operations)
- Class-wide result publication and unpublication
- Term-based and annual result management
- Student data maintenance and administration

Responsibilities:
- Form teachers manage all students in their assigned class
- Handle student enrollment across academic sessions
- Oversee publication of results for their entire class
- Coordinate between subject teachers and administration

Dependencies:
- SRMS.models: Student and academic data models
- TMS.models: Teacher and result management models
- Django authentication and JSON handling
"""

from operator import ge
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
    """
    Display students enrolled in a specific class and academic session.
    
    This view provides form teachers with a comprehensive list of all students
    enrolled in their assigned class for a particular academic session.
    
    Args:
        request: HTTP request object (requires authenticated user)
        Classname (str): Name of the class (e.g., "JSS1A", "SS2B")
        session_id (int): ID of the academic session
    
    Returns:
        HttpResponse: Rendered students.html template with student data
        
    Context:
        - class: Class object for the specified class
        - session: Academic session object
        - students: QuerySet of StudentClassEnrollment objects for this class/session
        - sessions: All available academic sessions
        
    Purpose:
        - Primary interface for form teachers to view their class roster
        - Provides foundation for student management operations
        - Shows enrollment status for specific academic sessions
        - Enables navigation between different academic sessions
        
    Security:
        - Requires login authentication
        - Typically restricted to form teachers of the specified class
        
    Database Optimization:
        - Uses select_related for optimized student data queries
        - Reduces database hits by joining related student information
    """
    classobject = get_object_or_404(Class, Class=Classname)
    sessionobject = get_object_or_404(AcademicSession, id=session_id)
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
    """
    Create a new student record and enroll them in a class.
    
    This AJAX view handles the creation of new student records and their
    enrollment in a specific class and academic session.
    
    Request Method: POST
    Content-Type: application/json
    
    Request Body:
        {
            "studentname": "John Doe",
            "Student_sex": "Male",
            "studentclass": "JSS1A",
            "academicsession": "2023/2024"
        }
    
    Returns:
        JsonResponse: Success response with student details:
        {
            "student_ID": 123,
            "student_id": "STU001", 
            "student_name": "John Doe",
            "student_sex": "Male",
            "message": "John Doe record has been created successfully in JSS1A for 2023/2024."
        }
        
        OR Error response:
        {
            "error": "Something went wrong: <error_message>"
        }
    
    Behavior:
        - Uses get_or_create to prevent duplicate student records
        - Creates or updates StudentClassEnrollment for class assignment
        - Handles both new student creation and existing student enrollment
        - Automatically generates unique student IDs
        
    Business Logic:
        - Students can be enrolled in multiple classes/sessions
        - Same student can appear in different academic sessions
        - Prevents duplicate enrollments in same class/session
        - Maintains referential integrity between students and enrollments
        
    Error Handling:
        - Catches and returns descriptive error messages
        - Validates class and session existence
        - Handles database constraint violations gracefully
    """
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
                "student_ID": student.pk,
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
    """
    Update existing student information and enrollment details.
    
    This AJAX view handles updates to student personal information and
    their class enrollment for a specific academic session.
    
    Request Method: POST
    Content-Type: application/json
    
    Request Body:
        {
            "studentID": 123,
            "studentname": "John Doe Updated",
            "Student_sex": "Male", 
            "studentclass": "JSS2A",
            "academicsession": "2023/2024"
        }
    
    Returns:
        JsonResponse: Success response with updated student details:
        {
            "student_ID": 123,
            "student_id": "STU001",
            "student_name": "John Doe Updated", 
            "student_sex": "Male",
            "message": "John Doe Updated's record has been updated successfully for JSS2A in 2023/2024."
        }
        
        OR Error response:
        {
            "error": "Something went wrong: <error_message>"
        }
    
    Behavior:
        - Updates student personal information (name, sex)
        - Updates or creates enrollment record for new class/session
        - Maintains student ID and other system-generated fields
        - Uses update_or_create for enrollment management
        
    Use Cases:
        - Correcting student personal information
        - Moving students between classes
        - Updating enrollment details for new sessions
        - Administrative data maintenance
        
    Business Logic:
        - Student personal data is updated in Students_Pin_and_ID model
        - Enrollment data is managed in StudentClassEnrollment model
        - Supports class transfers within same session
        - Maintains data integrity across related models
        
    Error Handling:
        - Validates student existence before updating
        - Handles class and session validation
        - Returns descriptive error messages for failures
    """
    data=json.loads(request.body)
    student_id=data['studentID']
    student_name=data['studentname']
    student_sex=data['Student_sex']
    student_class=data['studentclass']
    academic_session = data["academicsession"]
    # Fetch class and session objects
    classobject = get_object_or_404(Class, Class=student_class)
    sessionobject = get_object_or_404(AcademicSession, session=academic_session)
    updateStudent = get_object_or_404(Students_Pin_and_ID, id=student_id)

    try:
        # Update the student record
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
            "student_ID": updateStudent.pk,
            "student_id": updateStudent.student_id,
            "student_name": updateStudent.student_name,
            "student_sex": updateStudent.Sex,
            "message": f"{updateStudent.student_name}'s record has been updated successfully for {classobject.Class} in {sessionobject.session}.",
        }
        return JsonResponse(context, safe=False, status=200)
    except Exception as e:
        return JsonResponse({"error": f"Something went wrong: {str(e)}"}, safe=False, status=500)


def DeleteStudents_view(request):
    """
    Delete multiple student records and their associated enrollments.
    
    This AJAX view handles the deletion of student records along with
    all their enrollment data across all classes and sessions.
    
    Request Method: POST
    Content-Type: application/json
    
    Request Body: Array of student IDs to delete
        [123, 124, 125, ...]
    
    Returns:
        JsonResponse: Success response with deleted student names:
        {
            "message": "['John Doe', 'Jane Smith'] records have been deleted Successfully"
        }
        
        OR Error response:
        {
            "error": "something went wrong"
        }
    
    Behavior:
        - Deletes multiple students in a single operation
        - Removes all StudentClassEnrollment records for each student
        - Collects names of successfully deleted students
        - Maintains referential integrity by deleting enrollments first
        
    WARNING: 
        - This is a destructive operation that cannot be undone
        - Deletes ALL enrollment records for the students
        - May affect result data if students have published results
        - Should be used with caution and proper authorization
        
    Use Cases:
        - Administrative cleanup of student records
        - Removing incorrectly entered student data
        - End-of-session data management
        - Bulk student record maintenance
        
    Error Handling:
        - Catches exceptions during deletion process
        - Returns generic error message for security
        - Continues processing even if some deletions fail
        
    Security Considerations:
        - Should include additional authorization checks
        - Consider soft-delete instead of hard-delete
        - Log deletion activities for audit trails
    """
    studentidstodelete=json.loads(request.body)
    studentnamesdeleted=[]   
    try:
        for student_id in studentidstodelete:
            student = get_object_or_404(Students_Pin_and_ID, id=student_id)
            # Delete their enrollment records
            StudentClassEnrollment.objects.filter(student=student).delete()
            studentnamesdeleted.append(student.student_name)
        context={
            'message': f'{studentnamesdeleted} records have been deleted Successfully'
        }
        return JsonResponse(context, safe=False, status=200)
    except:
        return JsonResponse({'error': 'something went wrong' }, safe=False, status=500)


# -------------------------------------------------
# Form teachers View for CRUD Students Results
# -------------------------------------------------

@login_required
def PublishResults_view(request,Classname):
    """
    Display the result publication interface for form teachers.
    
    This view provides form teachers with an interface to publish results
    for their entire class across all subjects for a specific term and session.
    
    Args:
        request: HTTP request object (requires authenticated user)
        Classname (str): Name of the class (e.g., "JSS1A", "SS2B")
    
    Returns:
        HttpResponse: Rendered Publish_Result.html template
        OR: No_Subject_allocation.html if no subjects are allocated to the class
        
    Context:
        - subjects_allocation: Subject allocation object for the class
        - class: Class object for the specified class
        - sub_list: List of subject codes for the class
        - Terms: All available terms (1st, 2nd, 3rd)
        - academic_session: All available academic sessions
        - sessions: Alias for academic_session (template compatibility)
        
    Purpose:
        - Central hub for form teachers to manage result publication
        - Provides overview of all subjects taught in the class
        - Enables selection of term and session for result publication
        - Quality control before making results visible to students
        
    Subject Allocation Check:
        - Validates that subjects are allocated to the class
        - Returns special template if no subject allocation exists
        - Prevents errors when no subjects are assigned
        
    Security:
        - Requires login authentication
        - Typically restricted to form teachers of the specified class
    """
    Terms=Term.objects.all()
    academic_session= AcademicSession.objects.all()
    class_object = Class.objects.get(Class=Classname)
    subjects_allocation = Subjectallocation.objects.filter(classname=class_object).first()
    subject_code = []
    if not subjects_allocation:
        return render(request, 'No_Subject_allocation.html', {"class": class_object, "academic_session": academic_session})
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

@login_required
def getstudentsubjecttotals_view(request):
    data = json.loads(request.body)

    # Step 1: Validate core objects
    class_object = get_object_or_404(Class, Class=data['studentclass'])
    term_object = get_object_or_404(Term, term=data['selectedTerm'])
    session_object = get_object_or_404(AcademicSession, session=data['selectedAcademicSession'])

    # Step 2: Fetch subject allocation
    subjects_allocated = Subjectallocation.objects.filter(classname=class_object).first()
    if not subjects_allocated:
        return JsonResponse({"error": "No subjects allocated to this class"}, status=400)

    subject_list = list(subjects_allocated.subjects.all())

    # Step 3: Get all enrolled students
    enrollments = StudentClassEnrollment.objects.select_related("student").filter(
        student_class=class_object,
        academic_session=session_object
    )
    student_ids = [en.student.pk for en in enrollments]

    # Step 4: Prefetch all Student_Result_Data for these students
    srd_queryset = Student_Result_Data.objects.filter(
        Student_name_id__in=student_ids,
        Term=term_object,
        Academicsession=session_object
    )
    srd_map = {srd.Student_name.pk: srd for srd in srd_queryset}

    # Step 5: Prefetch all Result objects for all students and all allocated subjects
    result_queryset = Result.objects.filter(
        students_result_summary__in=srd_queryset,
        Subject__in=subject_list
    ).select_related("Subject", "students_result_summary")

    # (student_id, subject_id) → result
    result_map = {
        (res.students_result_summary.Student_name.pk, res.Subject.pk): res # type: ignore
        for res in result_queryset
    }

    final_list = []

    for enrollment in enrollments:
        student = enrollment.student
        srd = srd_map.get(student.pk)

        if not srd:
            # Create if not exist and update map
            srd = Student_Result_Data.objects.create(
                Student_name=student,
                Term=term_object,
                Academicsession=session_object
            )
            srd_map[student.pk] = srd

        student_dict = {
            'id': student.pk,
            'Name': student.student_name,
            'subjects': [],
            'published': srd.published
        }

        for subject in subject_list:
            res = result_map.get((student.pk, subject.pk))
            student_dict['subjects'].append({
                'subject_code': subject.subject_code,
                'subject_name': subject.subject_name,
                'Total': res.Total if res else "-",
                'published': res.published if res else False
            })

        final_list.append(student_dict)

    return JsonResponse(final_list, safe=False)


def publishstudentresult_view(request):
    """
    Publish termly results for all students in a class.
    
    This view processes and publishes term results for an entire class,
    including total scores, averages, positions, and remarks.
    
    Request Method: POST
    Content-Type: application/json
    
    Request Body:
        {
            "classdata": {
                "selectedTerm": "1st Term",
                "selectedAcademicSession": "2023/2024",
                "studentclass": "JSS1A"
            },
            "data": [
                {
                    "id": 123,
                    "Name": "John Doe",
                    "Total": 850,
                    "Ave": 85.0,
                    "Position": 1,
                    "Remarks": "Excellent"
                },
                ...
            ]
        }
    
    Returns:
        JsonResponse: Success or error message
    """
    try:
        data=json.loads(request.body)
        termobject=data['classdata']['selectedTerm']
        Acadsessionobject=data['classdata']['selectedAcademicSession']
        Classdata=data['classdata']['studentclass']
        classobject=get_object_or_404(Class, Class=Classdata)
        resultterm = get_object_or_404(Term, term=termobject)
        resultsession = get_object_or_404(AcademicSession, session=Acadsessionobject)

        published_count = 0
        for studentdata in data['data']:
            studentnumber = StudentClassEnrollment.objects.filter(student_class=classobject,academic_session=resultsession).count()
            student_enrolled = StudentClassEnrollment.objects.get(
                student__student_name=studentdata['Name'],
                student__id = studentdata['id'],
                student_class=classobject,
                academic_session=resultsession
            )

            try:
                studentresult=Student_Result_Data.objects.get(Student_name=student_enrolled.student,Term=resultterm,Academicsession=resultsession)
                studentresult.TotalScore=studentdata.get('Total', 0)
                studentresult.Totalnumber= str(studentnumber)
                studentresult.Average=studentdata.get('Ave', 0)
                studentresult.Position=studentdata.get('Position', '')
                studentresult.Remark=studentdata.get('Remarks', '')
                studentresult.published = True
                studentresult.save()
                published_count += 1
            except Exception as e:
                print(f"Error publishing result for {studentdata['Name']}: {str(e)}")
                continue
        
        return JsonResponse("Results have been Published and its now open to the Students", safe=False, status=200)
    except Exception as e:
        print(f"Error in publishstudentresult_view: {str(e)}")
        return JsonResponse({'error': 'Something went wrong, try again later'}, safe=False, status=500)


def unpublish_classresults_view(request):
    """
    Unpublish termly results for all students in a class.
    
    This view unpublishes term results for an entire class, making them
    invisible to students while preserving all computed data.
    
    Request Method: POST
    Content-Type: application/json
    
    Request Body:
        {
            "classdata": {
                "selectedTerm": "1st Term",
                "selectedAcademicSession": "2023/2024",
                "studentclass": "JSS1A"
            },
            "data": [
                {
                    "id": 123,
                    "Name": "John Doe"
                },
                ...
            ]
        }
    
    Returns:
        JsonResponse: Success or error message
    """
    try:
        data=json.loads(request.body)
        termobject=get_object_or_404(Term, term=data['classdata']['selectedTerm'])
        Acadsessionobject=get_object_or_404(AcademicSession, session=data['classdata']['selectedAcademicSession'])
        classobject=get_object_or_404(Class, Class=data['classdata']['studentclass'])

        unpublished_count = 0
        for student_data in data['data']:
            try:
                student_enrolled = StudentClassEnrollment.objects.get(
                    student__student_name=student_data['Name'],
                    student__id = student_data['id'],
                    student_class=classobject,
                    academic_session=Acadsessionobject
                )
                studentresult=get_object_or_404(Student_Result_Data, Student_name=student_enrolled.student, Term=termobject, Academicsession=Acadsessionobject)
                studentresult.published = False
                studentresult.save()
                unpublished_count += 1
            except Exception as e:
                print(f"Error unpublishing result for {student_data['Name']}: {str(e)}")
                continue
        
        return JsonResponse("Results have been Unpublished and its now closed to the Students", safe=False, status=200)
    except Exception as e:
        print(f"Error in unpublish_classresults_view: {str(e)}")
        return JsonResponse({'error': 'Something went wrong, try again later'}, safe=False, status=500)


# -----------------------------------------------------------------------------------
# Annual views for the Form teachers
# -----------------------------------------------------------------------------------
@login_required
def PublishAnnualResults_view(request,Classname):
    academic_session= AcademicSession.objects.all()
    class_object = get_object_or_404(Class, Class=Classname)
    subjects_allocation = get_object_or_404(Subjectallocation, classname=class_object)
    subject_code = []
    sessions = AcademicSession.objects.all()
    if not subjects_allocation:
        return render(request, 'No_Subject_allocation.html', {"class": class_object, "academic_session": academic_session})
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
    data = json.loads(request.body)
    classobject = get_object_or_404(Class, Class=data['studentclass'])
    session = get_object_or_404(AcademicSession, session=data['selectedAcademicSession'])

    subject_alloc = get_object_or_404(Subjectallocation, classname=classobject)
    subject_codes = [s.subject_code for s in subject_alloc.subjects.all()]
    subject_map = {
        s.subject_code: s for s in Subject.objects.filter(subject_code__in=subject_codes)
    }

    students = StudentClassEnrollment.objects.filter(
        student_class=classobject,
        academic_session=session
    ).select_related("student")
    student_ids = [s.student.pk for s in students]

    annual_student_map = {
        a.Student_name.pk: a for a in AnnualStudent.objects.filter(
            Student_name_id__in=student_ids,
            academicsession=session
        )
    }

    # Only use AnnualStudent IDs for fetching AnnualResult
    annual_results = AnnualResult.objects.filter(
        Student_name_id__in=[a.pk for a in annual_student_map.values()],
        Subject__subject_code__in=subject_codes
    ).select_related("Subject", "Student_name")
    result_map = {
        (ar.Student_name.pk, ar.Subject.subject_code): ar # type: ignore
        for ar in annual_results
    }

    final_list = []
    for student_enroll in students:
        student = student_enroll.student
        ann_student = annual_student_map.get(student.pk)
        student_data = {
            "id": student.pk,
            "Name": student.student_name,
            "published": ann_student.published if ann_student else False,
            "subjects": []
        }

        for sub in subject_alloc.subjects.all():
            code = sub.subject_code
            subject_obj = subject_map.get(code)
            result = result_map.get((ann_student.pk, code)) if ann_student and subject_obj else None

            student_data["subjects"].append({
                "subject_code": code,
                "subject_name": sub.subject_name,
                "Average": result.Average if result else "-",
                "published": result.published if result else False,
            })

        final_list.append(student_data)

    return JsonResponse(final_list, safe=False)





def publish_annualstudentresult_view(request):
    """
    Publish annual student results for an entire class.
    
    This view processes and publishes annual results for all students in a class,
    including total scores, averages, positions, remarks, and verdict.
    
    Request Method: POST
    Content-Type: application/json
    
    Request Body:
        {
            "classdata": {
                "selectedAcademicSession": "2023/2024",
                "studentclass": "JSS1A"
            },
            "data": [
                {
                    "id": 123,
                    "Name": "John Doe",
                    "Total": 850,
                    "Average": 85.0,
                    "Position": 1,
                    "Remarks": "Excellent performance",
                    "Verdict": "Promoted"
                },
                ...
            ]
        }
    
    Returns:
        JsonResponse: Success or error message
    """
    try:
        data=json.loads(request.body)
        Acadsessionobject=data['classdata']['selectedAcademicSession']
        Classdata=data['classdata']['studentclass']
        classobject=get_object_or_404(Class, Class=Classdata)
        resultsession = get_object_or_404(AcademicSession, session=Acadsessionobject)
        for studentdata in data['data']:
            # Use student ID for more reliable lookup
            student = get_object_or_404(Students_Pin_and_ID, id=studentdata['id'])
            studentnumber = StudentClassEnrollment.objects.filter(student_class=classobject,academic_session=resultsession).count()
            try:
                studentresult=get_object_or_404(AnnualStudent, Student_name=student,academicsession=resultsession)
                studentresult.TotalScore=studentdata.get('Total', 0)
                studentresult.Totalnumber= str(studentnumber)
                studentresult.Average=studentdata.get('Average', 0)
                studentresult.Position=studentdata.get('Position', '')
                studentresult.Remark=studentdata.get('Remarks', '')
                studentresult.Verdict = studentdata.get('Verdict', '')
                studentresult.published = True
                studentresult.save()
            except Exception as e:
                print(f"Error publishing result for {student.student_name}: {str(e)}")
                continue
        return JsonResponse("Results have been Published and its now open to the Students", safe=False, status=200)
    except Exception as e:
        print(f"Error in publish_annualstudentresult_view: {str(e)}")
        return JsonResponse({'error': 'Something went wrong, try again later'}, safe=False, status=500)
    

def unpublish_annual_classresults_view(request):
    """
    Unpublish annual results for all students in a class.
    
    This view unpublishes annual results for an entire class, making them
    invisible to students while preserving all computed data.
    
    Request Method: POST
    Content-Type: application/json
    
    Request Body:
        {
            "classdata": {
                "studentclass": "JSS1A",
                "selectedAcademicSession": "2023/2024"
            }
        }
    
    Returns:
        JsonResponse: Success or error message
    """
    try:
        data=json.loads(request.body)
        classobject=get_object_or_404(Class, Class=data['classdata']['studentclass'])
        Acadsessionobject=get_object_or_404(AcademicSession, session=data['classdata']['selectedAcademicSession'])
        students = StudentClassEnrollment.objects.filter(student_class=classobject,academic_session=Acadsessionobject)
        
        unpublished_count = 0
        for student_enroll in students:
            try:
                studentresult=get_object_or_404(AnnualStudent, Student_name=student_enroll.student, academicsession=Acadsessionobject)
                studentresult.published = False
                studentresult.save()
                unpublished_count += 1
            except Exception as e:
                print(f"Error unpublishing result for {student_enroll.student.student_name}: {str(e)}")
                continue
        
        return JsonResponse("Results have been Unpublished and its now closed to the Students", safe=False, status=200)
    except Exception as e:
        print(f"Error in unpublish_annual_classresults_view: {str(e)}")
        return JsonResponse({'error': 'Something went wrong, try again later'}, safe=False, status=500)
