"""
Computer-Based Testing (CBT) Views Module

This module contains views for managing Computer-Based Testing functionality.
Currently, most CBT features are disabled/commented out, but the infrastructure
remains for future implementation.

Key Features (Currently Disabled):
- CBT question management and creation
- Question set administration for different classes
- Answer validation and scoring
- Time-limited test configuration

Status: INACTIVE
- All CBT-related views are currently commented out
- Functionality preserved for future activation
- May require model updates before reactivation

Dependencies:
- SRMS.models: Student and academic data models
- TMS.models: Teacher models
- CBT.models: Computer-based testing models (commented out)
- Django authentication and Q objects for complex queries

Future Activation:
- Uncomment CBT.models import
- Verify model compatibility
- Test question and answer functionality
- Implement proper authentication and authorization
"""

from django.shortcuts import render, redirect, get_object_or_404
from SRMS.models import *
from ..models import *
from django.contrib.auth.decorators import login_required
# from CBT.models import *
from django.db.models import Q

# # CBT Teachers Views for CRUD and Submitting Questions
# @login_required
# def CBT_Questions_view(request,teachers_id):
#     """
#     Display CBT question management interface for teachers.
#     
#     This view would allow teachers to create and manage Computer-Based Test
#     questions for their subjects and assigned classes.
#     
#     CURRENTLY DISABLED - All CBT functionality is commented out
#     
#     Intended Functionality:
#     - Question creation and editing interface
#     - Subject and class selection for tests
#     - Time configuration for CBT sessions
#     - Question set management
#     
#     Args:
#         request: HTTP request object
#         teachers_id (int): ID of the teacher creating questions
#     
#     Returns:
#         HttpResponse: Would render CBT question management templates
#     """
#     subjects=Subject.objects.all()
#     classes=Class.objects.all()
#     teacher=Teacher.objects.get(id=teachers_id)

#     if request.method == 'POST':
#         classname = request.POST.getlist('test_classes')  # Assuming classname is a list
#         subject = Subject.objects.get(id=request.POST['subject'])
#         time = request.POST['testTime']

#         query = Q(subject=subject)
#         query &= Q(ExamClass__id__in=classname)

#         if QuestionSet.objects.filter(query).exists():
#             questionset = QuestionSet.objects.filter(query).order_by('-id').first()
#         else:
#             questionset = QuestionSet.objects.create(
#                 subject=subject,
#                 examTime=time,
#                 teacher=teacher
#             )
            
#             for class_id in classname:
#                 class_object = Class.objects.get(id=class_id)
#                 questionset.ExamClass.add(class_object)
#             questionset.save()
#         context = {'questionSet': questionset}
#         return render(request, 'CBT_Questions.html', context)

#     context={
#         "subjects":subjects,
#         "classes":classes,
#         "teacher":teacher
#     }
#     return render(request,'CBT_details.html',context)

# def CBT_update_details(request,id):
#     questionset = QuestionSet.objects.get(id=id)
#     if request.method == 'POST':
#         classname=request.POST.getlist('test_classes')
#         time=request.POST['testTime']
#         questionset.examTime = time
#         questionset.ExamClass.clear()
#         class_objects = Class.objects.filter(id__in=classname)
#         questionset.ExamClass.add(*class_objects)
#         questionset.save()
#         context={
#             'questionSet':questionset
#         }
#         return render(request,'CBT_Questions.html',context)
#     context={
#         "questionset":questionset
#     }
#     return render(request,'CBT_update_details.html',context)

# def submitquestion_view(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         subject_name = data.get('subject')
#         teacher_name = data.get('teacher')
#         exam_time = data.get('examTime')
#         classes = data.get('Class')

#         # Get or create Subject and Teacher instances
#         subject = Subject.objects.get(subject_name=subject_name)
#         teacher = Teacher.objects.filter(FirstName=teacher_name).first()
#         query = Q(subject=subject)
#         query &= Q(ExamClass__id__in=classes)

#         if QuestionSet.objects.filter(query).exists():
#             question_set = QuestionSet.objects.filter(query).order_by('-id').first()
#         else:
#             question_set = QuestionSet.objects.create(
#                 examTime=exam_time,
#                 teacher=teacher,
#                 subject=subject
#             )
#             for class_name in classes:
#                 class_obj, created = Class.objects.get_or_create(Class=class_name)
#                 question_set.ExamClass.add(class_obj)
#             question_set.save()
#         questions_data = data['questions']
#         for question_data in questions_data:
#             question_id = question_data.get('id')
#             required = question_data.get('questionrequired')
#             # get the Question and set its required property
#             question = Question.objects.get(
#                 questionId =question_id,
#             )
#             question.required=required
#             question.save()
#             # get the nswers and set its is_correct property
#             answers_data = question_data['answers']
#             for answer_data in answers_data:
#                 answer_id = answer_data.get('id')
#                 is_correct = answer_data.get('isCorrect')

#                 answer = Answer.objects.get(
#                     answerId=answer_id,
#                 )
#                 answer.isCorrect=is_correct
#                 answer.save()
#                 question.answers.add(answer)

#             question_set.questions.add(question)

#         return JsonResponse({'message': 'Questions and answers submitted successfully'})  # Return a success response

#     return JsonResponse({'error': 'Invalid request method'})


# ////////////////////////////







	
