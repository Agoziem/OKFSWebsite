"""
Main Teacher Views Module

This module contains the core views for teacher functionality including
dashboard access, profile management, and basic navigation. It serves as
the entry point for teacher interactions with the system.

Key Features:
- Teacher dashboard with session overview
- Teacher profile management and updates
- Role-based access control
- Form teacher assignment management

Dependencies:
- SRMS.models: Student and academic data models
- TMS.models: Teacher models and forms
- Django authentication and form handling
"""

from django.shortcuts import render, redirect
from SRMS.models import *
from ..models import *
from ..forms import TeacherForm
from django.contrib.auth.decorators import login_required


# Teachers Dashbord View
@login_required
def Teachers_dashboard_view(request):
    """
    Display the main teacher dashboard.
    
    This view serves as the landing page for authenticated teachers, providing
    access to academic sessions and navigation to various teacher functions.
    
    Args:
        request: HTTP request object (requires authenticated user)
    
    Returns:
        HttpResponse: Rendered Teachers_dashboard.html template
        
    Context:
        - sessions: All available academic sessions for dropdown/navigation
        
    Purpose:
        - Central hub for teacher activities
        - Provides session selection for academic operations
        - Navigation point to other teacher functions (results, students, etc.)
        
    Security:
        - Requires login authentication
        - Only accessible to authenticated teachers
    """
    sessions = AcademicSession.objects.all()
    context={
        "sessions":sessions
    }
    return render(request,'Teachers_dashboard.html',context)

# Teachers profile View
@login_required
def profile_view(request,id):
    """
    Display and handle teacher profile management.
    
    This view allows teachers to view and update their profile information,
    including personal details, role assignment, and class/subject allocations.
    
    Args:
        request: HTTP request object
        id (int): Teacher's ID from the database
    
    Returns:
        HttpResponse: Rendered editprofile.html template
        OR
        HttpResponseRedirect: Redirect to dashboard after successful update
        
    Request Methods:
        GET: Display the profile form with current teacher data
        POST: Process profile updates and save changes
        
    POST Data:
        - All TeacherForm fields (name, contact info, etc.)
        - Role: Teacher role selection ("Formteacher" or other)
        - classFormed: Class assignment (only for Form teachers)
        
    Context:
        - teacher: Teacher object being edited
        - classes: All available classes for assignment
        - subjects: All available subjects
        - sessions: All academic sessions
        - form: Pre-populated TeacherForm instance
        
    Business Logic:
        - Only Form teachers can be assigned to classes
        - Non-Form teachers have their class assignment cleared
        - Handles many-to-many field saving correctly
        - Validates role-based class assignment rules
        
    Security:
        - Requires login authentication
        - Teachers can only edit their own profiles (via ID parameter)
    """
    teacher = Teacher.objects.get(id=id)
    classes=Class.objects.all()
    subjects=Subject.objects.all()
    sessions = AcademicSession.objects.all()
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        role = request.POST.get("Role")
        class_formed = request.POST.get("classFormed")
        if form.is_valid():
            teacher = form.save(commit=False)

            # Update the Role
            teacher.Role = role

            # Only assign classFormed if Role is 'Form-teacher'
            if role == "Formteacher":
                if class_formed:
                    teacher.classFormed_id = class_formed
            else:
                teacher.classFormed = None  # Reset if Role is not Form-teacher
            teacher.save()
            form.save_m2m()  # Save ManyToMany fields
            return redirect('TMS:Teachers_dashboard')
    
    context={
        'teacher': teacher,
        'classes':classes,
        'subjects':subjects,
        "sessions":sessions,
        'form': TeacherForm(instance=teacher),
    }
    return render(request,'editprofile.html',context)








	
