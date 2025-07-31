"""
Administrative Views Module

This module contains views specifically designed for school administrators to
monitor and oversee result publication across all classes and subjects. It provides
a high-level overview of result status and publication management.

Key Features:
- School-wide result monitoring for termly results
- Annual result overview across all classes
- Publication status tracking by class and subject
- Administrative oversight of result publication workflow

Dependencies:
- SRMS.models: Student and academic data models
- TMS.models: Teacher and result management models
- Django HTTP response and authentication utilities
"""

from django.shortcuts import render,get_object_or_404
from requests import get
from SRMS.models import *
from ..models import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import json

def schoolresult_view(request):
    """
    Display the school-wide result monitoring dashboard for termly results.
    
    This view provides administrators with an interface to monitor result
    publication status across all classes, terms, and academic sessions.
    
    Args:
        request: HTTP request object
    
    Returns:
        HttpResponse: Rendered schoolresults.html template
        
    Context:
        - school_classes: All classes in the school
        - academic_session: All available academic sessions
        - terms: All academic terms (1st, 2nd, 3rd)
        - sessions: Alias for academic_session (template compatibility)
        
    Purpose:
        - Provides administrative oversight of result publication
        - Allows monitoring of which results are published/unpublished
        - Enables selection of specific class/term/session combinations
        - Central dashboard for result management oversight
    """
    school_classes = Class.objects.all()
    academic_session = AcademicSession.objects.all()
    terms = Term.objects.all()
    context = {
        'school_classes': school_classes,
        'academic_session': academic_session,
        'terms': terms,
        'sessions':academic_session
    }
    return render(request,'schoolresults.html',context)

def getclasspublishedResults(request):
    """
    Retrieve publication status of results for a specific class, term, and session.
    
    This AJAX view provides detailed information about which subjects have
    published results for a given class and academic period.
    
    Request Method: POST
    Content-Type: application/json
    
    Request Body:
        {
            "classname": "JSS1A",
            "term": "1st Term", 
            "session": "2023/2024"
        }
    
    Returns:
        JsonResponse: Object containing class result publication status:
        {
            "classname": "JSS1A",
            "published": true/false,  // Overall class publication status
            "subjects": [
                {
                    "subject": "Mathematics",
                    "published": true/false
                },
                {
                    "subject": "English", 
                    "published": false
                },
                ...
            ]
        }
    
    OR Error Response:
        {
            "error": "No students found for this class and academic session"
        }
        
    Behavior:
        - Checks if any students are enrolled in the specified class/session
        - Gets overall publication status from Student_Result_Data
        - Iterates through all allocated subjects for the class
        - Returns individual subject publication status
        - Handles missing result data gracefully
        
    Error Handling:
        - Returns 404 if no students found in class/session
        - Returns empty subjects array if no result data exists
        - Catches and logs exceptions, returns 500 for server errors
        
    Use Case:
        - Administrative monitoring of result publication progress
        - Identifying which subjects still need result publication
        - Quality assurance for result management workflow
    """
    try:
        data = json.loads(request.body)
        classobject = get_object_or_404(Class, Class=data['classname'])
        termobject = get_object_or_404(Term, term=data['term'])
        academic_sessionobject = get_object_or_404(AcademicSession, session=data['session'])
        subject_allocations = get_object_or_404(Subjectallocation, classname=classobject)
        classstudent = StudentClassEnrollment.objects.filter(student_class=classobject,academic_session=academic_sessionobject).first()
        classresultdata = {}
        if not classstudent:
            return JsonResponse({'error': 'No students found for this class and academic session'}, status=404)
        try:
            resultsummary = Student_Result_Data.objects.get(Student_name=classstudent.student,Term=termobject,Academicsession=academic_sessionobject)
            classresultdata["classname"] =  classobject.Class
            classresultdata['published'] = resultsummary.published
            subjectResults = []
            for subject in subject_allocations.subjects.all():
                Subjectresult = {}
                try:
                    subject_results = get_object_or_404(Result, students_result_summary=resultsummary,Subject=subject)
                    Subjectresult['subject'] = subject.subject_name
                    Subjectresult['published'] = subject_results.published
                except:
                    Subjectresult['subject'] = subject.subject_name
                    Subjectresult['published'] = False
                subjectResults.append(Subjectresult)
            classresultdata['subjects'] = subjectResults
            return JsonResponse(classresultdata, safe=False)
        except:
            classresultdata["classname"] =  classobject.Class
            classresultdata['published'] = False
            classresultdata['subjects'] = []
            return JsonResponse(classresultdata, safe=False)
    except Exception as e:
        print(e)
        return JsonResponse({'error': 'An error occured try again later'}, safe=False, status=500)
    
# Admin annual View of School Results
def schoolannualresult_view(request):
    """
    Display the school-wide annual result monitoring dashboard.
    
    This view provides administrators with an interface to monitor annual
    result publication status across all classes and academic sessions.
    
    Args:
        request: HTTP request object
    
    Returns:
        HttpResponse: Rendered schoolannualresults.html template
        
    Context:
        - school_classes: All classes in the school
        - academic_session: All available academic sessions
        - sessions: Alias for academic_session (template compatibility)
        
    Purpose:
        - Administrative oversight of annual result publication
        - Monitoring annual result compilation across the school
        - Quality assurance for end-of-year result processing
        - Central dashboard for annual result management
        
    Difference from schoolresult_view:
        - Focuses on annual results (aggregated across all terms)
        - Does not include term selection (annual results span full session)
        - Used for end-of-year result monitoring and publication
    """
    school_classes = Class.objects.all()
    academic_session = AcademicSession.objects.all()
    context = {
        'school_classes': school_classes,
        'academic_session': academic_session,
        'sessions':academic_session
    }
    return render(request,'schoolannualresults.html',context)

def getclassannualpublishedResults(request):
    """
    Retrieve publication status of annual results for a specific class and session.
    
    This AJAX view provides detailed information about which subjects have
    published annual results for a given class and academic session.
    
    Request Method: POST
    Content-Type: application/json
    
    Request Body:
        {
            "classname": "JSS1A",
            "session": "2023/2024"
        }
    
    Returns:
        JsonResponse: Object containing class annual result publication status:
        {
            "classname": "JSS1A", 
            "published": true/false,  // Overall annual publication status
            "subjects": [
                {
                    "subject": "Mathematics",
                    "published": true/false
                },
                {
                    "subject": "English",
                    "published": false  
                },
                ...
            ]
        }
    
    OR Error Response:
        {
            "error": "No students found for this class and academic session"
        }
        
    Behavior:
        - Checks if any students are enrolled in the specified class/session
        - Gets overall annual publication status from AnnualStudent
        - Iterates through all allocated subjects for the class
        - Returns individual subject annual publication status
        - Handles missing annual result data gracefully
        
    Error Handling:
        - Returns 404 if no students found in class/session
        - Returns empty subjects array if no annual result data exists
        - Catches and logs exceptions for debugging
        
    Use Case:
        - Administrative monitoring of annual result publication progress
        - End-of-year result management oversight
        - Identifying which subjects need annual result compilation
        - Quality assurance for annual result workflow
        
    Difference from getclasspublishedResults:
        - Works with AnnualStudent and AnnualResult models
        - No term parameter (annual results span entire session)
        - Focused on year-end result aggregation status
    """
    try:
        data = json.loads(request.body)
        classobject = get_object_or_404(Class, Class=data['classname'])
        academic_sessionobject = get_object_or_404(AcademicSession, session=data['session'])
        subject_allocations = get_object_or_404(Subjectallocation, classname=classobject)
        classstudent = StudentClassEnrollment.objects.filter(student_class=classobject,academic_session=academic_sessionobject).first()
        classannualresultdata = {}
        if not classstudent:
            return JsonResponse({'error': 'No students found for this class and academic session'}, status=404)
        try:
            annualresultsummary = get_object_or_404(AnnualStudent, Student_name=classstudent.student,academicsession=academic_sessionobject)
            classannualresultdata["classname"] =  classobject.Class
            classannualresultdata['published'] = annualresultsummary.published
            annualsubjectResults = []
            for subject in subject_allocations.subjects.all():
                Subjectresult = {}
                try:
                    subject_results = get_object_or_404(AnnualResult, Student_name=annualresultsummary, Subject=subject)
                    Subjectresult['subject'] = subject.subject_name
                    Subjectresult['published'] = subject_results.published
                except:
                    Subjectresult['subject'] = subject.subject_name
                    Subjectresult['published'] = False
                annualsubjectResults.append(Subjectresult)
            classannualresultdata['subjects'] = annualsubjectResults
        except:
            classannualresultdata["classname"] =  classobject.Class
            classannualresultdata['published'] = False
            classannualresultdata['subjects'] = []
        return JsonResponse(classannualresultdata, safe=False)
    except Exception as e:
        print(e)
        return JsonResponse({'error': 'An error occured try again later'}, safe=False)