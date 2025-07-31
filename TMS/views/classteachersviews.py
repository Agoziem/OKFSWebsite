"""
Class Teachers Views Module

This module contains views specifically designed for class teachers to manage student results
and perform result computations. It handles both termly and annual result management including
data entry, computation, and publication.

Key Features:
- Term-based result computation and management
- Annual result computation across all terms
- Student result data entry and updates
- Result publication and unpublication
- Grade and position calculation

Dependencies:
- SRMS.models: Student and academic data models
- TMS.models: Teacher and result management models
- Django authentication and JSON handling
"""
from django.shortcuts import render,get_object_or_404
from SRMS.models import *
from ..models import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
# from CBT.models import *
import json

@login_required
def result_computation_view(request,Classname,id):
    """
    Display the result computation interface for class teachers.
    
    This view renders the main result computation page where teachers can select
    terms, academic sessions, and subjects to enter student results.
    
    Args:
        request: HTTP request object
        Classname (str): Name of the class (e.g., "JSS1A", "SS2B")
        id (int): Teacher's ID from the database
    
    Returns:
        HttpResponse: Rendered Result_computation.html template with context data
        
    Context:
        - class: Class object for the specified class
        - Terms: All available terms (1st, 2nd, 3rd)
        - academic_session: All available academic sessions
        - subjects_taught_for_class: Subjects this teacher teaches for this class
        - sessions: Alias for academic_session (for template compatibility)
    
    Raises:
        Http404: If teacher or class is not found
    """
    teacher = get_object_or_404(Teacher, id=id)
    Terms=Term.objects.all()
    academic_session= AcademicSession.objects.all()
    classobject = get_object_or_404(Class, Class=Classname)
    subjectsforclass= get_object_or_404(Subjectallocation, classname=classobject)
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
    """
    Retrieve student results for a specific class, subject, term and session.
    
    This AJAX view fetches all students enrolled in a class and their existing
    result data for the specified subject and term. Creates result records if
    they don't exist.
    
    Request Method: POST
    Content-Type: application/json
    
    Request Body:
        {
            "studentclass": "JSS1A",
            "studentsubject": "Mathematics", 
            "selectedTerm": "1st Term",
            "selectedAcademicSession": "2023/2024"
        }
    
    Returns:
        JsonResponse: List of student result objects with the following structure:
        [
            {
                "Name": "Student Full Name",
                "1sttest": 15,
                "1stAss": 10,
                "Project": 5,
                "MidTermTest": 20,
                "2ndTest": 18,
                "2ndAss": 12,
                "Exam": 45,
                "studentID": "STU001",
                "published": false
            },
            ...
        ]
    
    Behavior:
        - Creates Student_Result_Data and Result objects if they don't exist
        - Uses get_or_create to avoid duplicate records
        - Skips students without result data and logs to console
        - Returns empty scores for new result records
    """
    data=json.loads(request.body)
    studentResults = []
    classobject = get_object_or_404(Class, Class=data['studentclass'])
    subjectobject = get_object_or_404(Subject, subject_name=data['studentsubject'])
    term = get_object_or_404(Term, term=data['selectedTerm'])
    session = get_object_or_404(AcademicSession, session=data['selectedAcademicSession'])
    students = StudentClassEnrollment.objects.filter(student_class=classobject, academic_session=session)

    for studentresult in students:
        student_result_details, created = Student_Result_Data.objects.get_or_create(Student_name=studentresult.student, Term=term, Academicsession=session)
        student_result_object, created = Result.objects.get_or_create(Subject=subjectobject, students_result_summary=student_result_details)
        if student_result_object.students_result_summary:
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
        else:
            print(f"No result found for {studentresult.student.student_name} in {term.term} term for {subjectobject.subject_name}.")
            continue
    return JsonResponse(studentResults, safe=False, status=200)

@login_required
def update_student_result_view(request):
    """
    Update individual student result data for a specific subject and term.
    
    This AJAX view handles updates to a single student's result data including
    test scores, assignments, projects, and exam scores.
    
    Request Method: POST
    Content-Type: application/json
    
    Request Body:
        {
            "classdata": {
                "selectedTerm": "1st Term",
                "selectedAcademicSession": "2023/2024", 
                "studentsubject": "Mathematics"
            },
            "formDataObject": {
                "studentID": "STU001",
                "Name": "John Doe",
                "1sttest": 15,
                "1stAss": 10,
                "Project": 5,
                "MidTermTest": 20,
                "2ndAss": 12,
                "2ndTest": 18,
                "Exam": 45
            }
        }
    
    Returns:
        JsonResponse: Success message confirming the update
        
    Behavior:
        - Validates student, subject, term and session exist
        - Updates all assessment scores in the Result model
        - Does not calculate totals or grades (handled separately)
        - Saves changes to database immediately
    
    Raises:
        Http404: If any of the required objects (student, subject, term, session) don't exist
    """
    data=json.loads(request.body)
    term=get_object_or_404(Term, term=data['classdata']['selectedTerm'])
    session=get_object_or_404(AcademicSession, session=data['classdata']['selectedAcademicSession'])
    studentobject= get_object_or_404(Students_Pin_and_ID, student_id=data['formDataObject']['studentID'], student_name=data['formDataObject']['Name'])
    subjectobject = get_object_or_404(Subject, subject_name=data['classdata']['studentsubject'])
    student_result_details = get_object_or_404(Student_Result_Data, Student_name=studentobject, Term=term, Academicsession=session)
    studentResult = get_object_or_404(Result, students_result_summary=student_result_details, Subject=subjectobject)
    studentResult.FirstTest  = data['formDataObject']['1sttest']
    studentResult.FirstAss  = data['formDataObject']['1stAss']
    studentResult.Project  = data['formDataObject']['Project']
    studentResult.MidTermTest  = data['formDataObject']['MidTermTest']
    studentResult.SecondAss = data['formDataObject']['2ndAss']
    studentResult.SecondTest = data['formDataObject']['2ndTest']
    studentResult.Exam = data['formDataObject']['Exam']
    studentResult.save()

    return JsonResponse('Result Updated Successfully', safe=False, status=200)
    

def submitallstudentresult_view(request):
    """
    Submit and publish complete results for all students in a class/subject.
    
    This view handles the final submission of computed results including calculated
    grades, positions, and remarks. It processes all students at once and marks
    their results as published.
    
    Request Method: POST
    Content-Type: application/json
    
    Request Body:
        {
            "classdata": {
                "studentsubject": "Mathematics",
                "selectedTerm": "1st Term", 
                "selectedAcademicSession": "2023/2024"
            },
            "data": [
                {
                    "studentID": "STU001",
                    "Name": "John Doe",
                    "1sttest": 15,
                    "1stAss": 10,
                    "Project": 5,
                    "MidTermTest": 20,
                    "2ndTest": 18,
                    "2ndAss": 12,
                    "CA": 50,
                    "Exam": 45,
                    "Total": 95,
                    "Grade": "A",
                    "Position": 1,
                    "Remarks": "Excellent"
                },
                ...
            ]
        }
    
    Returns:
        JsonResponse: Success message confirming results submission
        
    Behavior:
        - Updates all assessment scores and computed values
        - Sets published=True to make results visible to students
        - Processes all students in a single transaction
        - Includes continuous assessment (CA), total, grade, position and remarks
        
    Note:
        - This is typically the final step after all calculations are done
        - Once published, results become visible to students and parents
    """
    data=json.loads(request.body)
    for result in data['data']:
        subjectobject = get_object_or_404(Subject, subject_name=data['classdata']['studentsubject'])
        term = get_object_or_404(Term, term=data['classdata']['selectedTerm'])
        session = get_object_or_404(AcademicSession, session=data['classdata']['selectedAcademicSession'])
        studentobject= get_object_or_404(Students_Pin_and_ID, student_id=result['studentID'], student_name=result['Name'])
        student_result_details = get_object_or_404(Student_Result_Data, Student_name=studentobject, Term=term, Academicsession=session)
        studentResult = get_object_or_404(Result, students_result_summary=student_result_details, Subject=subjectobject)
        fields = {
            '1sttest': 'FirstTest',
            '1stAss': 'FirstAss',
            'Project': 'Project',
            'MidTermTest': 'MidTermTest',
            '2ndTest': 'SecondAss',
            '2ndAss': 'SecondTest',
            'CA': 'CA',
            'Exam': 'Exam',
            'Total': 'Total',
            'Grade': 'Grade',
            'Position': 'SubjectPosition',
            'Remarks': 'Remark',
        }
        for key, attr in fields.items():
            setattr(studentResult, attr, result[key])
        studentResult.published=True
        studentResult.save()
    return JsonResponse('Results submitted Successfully', safe=False, status=200)


def unpublish_results_view(request):
    """
    Unpublish results to hide them from students.
    
    This view allows teachers to unpublish results, making them invisible
    to students while preserving the data for future republishing.
    
    Request Method: POST
    Content-Type: application/json
    
    Request Body:
        {
            "classdata": {
                "selectedTerm": "1st Term",
                "selectedAcademicSession": "2023/2024",
                "studentsubject": "Mathematics"
            },
            "data": [
                {
                    "Name": "John Doe",
                    "studentID": "STU001"
                },
                ...
            ]
        }
    
    Returns:
        JsonResponse: Success message confirming results have been unpublished
        
    Behavior:
        - Sets published=False for all specified student results
        - Preserves all result data (scores, grades, etc.)
        - Continues processing even if some students have errors
        - Results become invisible to students immediately
        
    Error Handling:
        - Catches and logs exceptions for individual students
        - Continues processing remaining students if one fails
        - Uses try-except to handle missing result records gracefully
    """
    data=json.loads(request.body)
    for studentdata in data['data']:
        resultterm = get_object_or_404(Term, term=data['classdata']['selectedTerm'])
        resultsession = get_object_or_404(AcademicSession, session=data['classdata']['selectedAcademicSession'])
        subjectobject = get_object_or_404(Subject, subject_name=data['classdata']['studentsubject'])
        student = get_object_or_404(Students_Pin_and_ID, student_name=studentdata['Name'], student_id=studentdata['studentID'])
        try:
            student_result_details=get_object_or_404(Student_Result_Data, Student_name=student, Term=resultterm, Academicsession=resultsession)
            studentResult = get_object_or_404(Result, students_result_summary=student_result_details, Subject=subjectobject)
            studentResult.published = False
            studentResult.save()
        except Exception as e:
            print(str(e))
            continue
    return JsonResponse('Results have been unpublished and its no longer opened to the Students', safe=False, status=200)


# ---------------------------------
# Annual Result Computation Views
# ---------------------------------

def annualresult_computation(request,Classname,id):
    """
    Display the annual result computation interface for class teachers.
    
    This view renders the page where teachers can work with annual results that
    combine data from all three terms of an academic session.
    
    Args:
        request: HTTP request object
        Classname (str): Name of the class (e.g., "JSS1A", "SS2B")
        id (int): Teacher's ID from the database
    
    Returns:
        HttpResponse: Rendered Annual_Results.html template with context data
        
    Context:
        - class: Class object for the specified class
        - academic_session: All available academic sessions
        - subjects_taught_for_class: Subjects this teacher teaches for this class
        - sessions: Alias for academic_session (for template compatibility)
    
    Purpose:
        - Provides interface for annual result computation
        - Shows teacher's assigned subjects for the class
        - Allows selection of academic session for annual results
    """
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
    """
    Retrieve and compute annual results by aggregating termly results.
    
    This AJAX view processes annual result data by combining results from all
    three terms (1st, 2nd, 3rd) for each student in a specific subject and class.
    
    Request Method: POST
    Content-Type: application/json
    
    Request Body:
        {
            "selectedAcademicSession": "2023/2024",
            "studentclass": "JSS1A", 
            "studentsubject": "Mathematics"
        }
    
    Returns:
        JsonResponse: List of student annual result objects with structure:
        [
            {
                "studentID": "STU001",
                "Name": "John Doe",
                "terms": {
                    "1st Term": 85,
                    "2nd Term": 78,
                    "3rd Term": 92
                },
                "published": false
            },
            ...
        ]
    
    Behavior:
        - Creates AnnualStudent and AnnualResult objects if they don't exist
        - Fetches termly totals from Result model for each term
        - Handles missing term results by showing "-"
        - Aggregates all term data into a single response
        - Shows publication status for annual results
        
    Data Flow:
        1. Get enrolled students for the class and session
        2. For each student, create/get annual result record
        3. For each term, fetch the student's result total
        4. Compile term totals into a dictionary structure
        5. Return combined data with publication status
        
    Error Handling:
        - Gracefully handles missing Student_Result_Data or Result objects
        - Shows "-" for terms with no data
        - Logs missing results to console for debugging
    """
    data = json.loads(request.body)
    print(data)
    session = get_object_or_404(AcademicSession, session=data['selectedAcademicSession'])
    class_object = get_object_or_404(Class, Class=data['studentclass'])
    subject_object = get_object_or_404(Subject, subject_name=data['studentsubject'])
    students = StudentClassEnrollment.objects.filter(student_class=class_object,academic_session=session)
    terms = Term.objects.all()
    students_annuals = []

    for student in students:
        studentAnnual,created = AnnualStudent.objects.get_or_create(Student_name=student.student, academicsession=session)
        student_annual_details, created = AnnualResult.objects.get_or_create(Student_name=studentAnnual, Subject=subject_object)
        student_annual_details.Total = str(0)  # Ensure Total is initialized to zero
        termsobject = {}  # Reset for each student
        for term in terms:
            try:
                student_result_details, created = Student_Result_Data.objects.get_or_create(Student_name=student.student, Term=term, Academicsession=session)
                student_result, created = Result.objects.get_or_create(students_result_summary=student_result_details, Subject=subject_object)
                termsobject[term.term] = student_result.Total
            except (Student_Result_Data.DoesNotExist, Result.DoesNotExist):
                print(f"No result found/created for {student.student.student_name} in {term.term} term for {subject_object.subject_name}.")
                termsobject[term.term] = "-"  # Handle missing results gracefully
            students_annuals.append({
                "studentID": student.student.student_id,
                'Name': student.student.student_name,
                'terms': termsobject,
                'published': student_annual_details.published
            })
    
    return JsonResponse(students_annuals, safe=False)


def publish_annual_results(request):
    """
    Publish computed annual results to make them visible to students.
    
    This view processes and publishes annual results that have been computed
    from termly data, including totals, averages, grades, and positions.
    
    Request Method: POST
    Content-Type: application/json
    
    Request Body:
        {
            "classdata": {
                "studentsubject": "Mathematics",
                "studentclass": "JSS1A",
                "selectedAcademicSession": "2023/2024"
            },
            "data": [
                {
                    "studentID": "STU001", 
                    "Name": "John Doe",
                    "terms": {
                        "1st Term": "85",
                        "2nd Term": "78", 
                        "3rd Term": "92"
                    },
                    "Total": 255,
                    "Average": 85.0,
                    "Grade": "A",
                    "Position": 1,
                    "Remarks": "Excellent performance"
                },
                ...
            ]
        }
    
    Returns:
        JsonResponse: Success message confirming annual results publication
        
    Behavior:
        - Updates AnnualResult model with computed values
        - Stores individual term totals and overall statistics
        - Sets published=True to make results visible to students
        - Processes all students in the class for the subject
        
    Data Stored:
        - FirstTermTotal, SecondTermTotal, ThirdTermTotal: Individual term scores
        - Total: Sum of all three terms
        - Average: Mean score across terms
        - Grade: Letter grade based on average
        - SubjectPosition: Rank within the class for this subject
        - Remark: Qualitative assessment comment
        
    Usage:
        - Called after annual computation and grading is complete
        - Makes annual results accessible to students and parents
        - Typically used at the end of an academic session
    """
    data = json.loads(request.body)
    subject_object = get_object_or_404(Subject, subject_name=data['classdata']['studentsubject'])
    class_object = get_object_or_404(Class, Class=data['classdata']['studentclass'])
    session = get_object_or_404(AcademicSession, session=data['classdata']['selectedAcademicSession'])
    for result in data['data']:
        student = get_object_or_404(Students_Pin_and_ID, student_id=result['studentID'], student_name=result['Name'])
        studentAnnual = get_object_or_404(AnnualStudent, Student_name=student, academicsession=session)
        student_annual_details = get_object_or_404(AnnualResult, Student_name=studentAnnual, Subject=subject_object)
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
    return JsonResponse('Results have been published', safe=False, status=200)


def unpublish_annual_results(request):
    """
    Unpublish annual results to hide them from students.
    
    This view allows teachers to unpublish annual results, making them invisible
    to students while preserving all computed data for future republishing.
    
    Request Method: POST
    Content-Type: application/json
    
    Request Body:
        {
            "classdata": {
                "studentsubject": "Mathematics",
                "studentclass": "JSS1A", 
                "selectedAcademicSession": "2023/2024"
            },
            "data": [
                {
                    "Name": "John Doe"
                },
                ...
            ]
        }
    
    Returns:
        JsonResponse: Success message confirming annual results have been unpublished
        
    Behavior:
        - Sets published=False for all specified student annual results
        - Preserves all computed data (totals, averages, grades, positions)
        - Results become invisible to students immediately
        - Data remains available for future republishing
        
    Purpose:
        - Allows corrections to be made before final publication
        - Provides control over when annual results are visible
        - Enables review and verification before student access
        
    Note:
        - Only affects the publication status, not the underlying data
        - Results can be republished later without recalculation
        - Useful for quality control and administrative review
    """
    data = json.loads(request.body)
    subject_object = get_object_or_404(Subject, subject_name=data['classdata']['studentsubject'])
    class_object = get_object_or_404(Class, Class=data['classdata']['studentclass'])
    session = get_object_or_404(AcademicSession, session=data['classdata']['selectedAcademicSession'])
    for studentdata in data['data']:
        student = get_object_or_404(Students_Pin_and_ID, student_name=studentdata['Name'])
        studentAnnual = get_object_or_404(AnnualStudent, Student_name=student, academicsession=session)
        student_annual_details = get_object_or_404(AnnualResult, Student_name=studentAnnual, Subject=subject_object)
        student_annual_details.published = False
        student_annual_details.save()
    return JsonResponse('Results have been unpublished', safe=False, status=200)


	
