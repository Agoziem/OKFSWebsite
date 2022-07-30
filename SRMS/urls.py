from django.urls import path
from django.conf.urls import url
from .views import *
app_name = 'SRMS'
urlpatterns = [
    path('', classes_view, name='classes'),
    path('activation/', activation_view, name='activation'),
    path('activation/createjuniorstudents1a/', createjuniorstudent1a_view, name='juniorstudents1a'),
    path('activation/createjuniorstudents1b/', createjuniorstudent1b_view, name='juniorstudents1b'),
    path('activation/createjuniorstudents1c/', createjuniorstudent1c_view, name='juniorstudents1c'),
    path('activation/createjuniorstudents2a/', createjuniorstudent2a_view, name='juniorstudents2a'),
    path('activation/createjuniorstudents2b/', createjuniorstudent2b_view, name='juniorstudents2b'),
    path('activation/createjuniorstudents3/', createjuniorstudent3_view, name='juniorstudents3'),
    path('activation/createjuniorresults1a/', createjuniorresult1a_view, name='juniorresult1a'),
    path('activation/createjuniorresults1b/', createjuniorresult1b_view, name='juniorresult1b'),
    path('activation/createjuniorresults1c/', createjuniorresult1c_view, name='juniorresult1c'),
    path('activation/createjuniorresults2a/', createjuniorresult2a_view, name='juniorresult2a'),
    path('activation/createjuniorresults2b/', createjuniorresult2b_view, name='juniorresult2b'),
    path('activation/createjuniorresults3/', createjuniorresult3_view, name='juniorresult3'),
    path('activation/createseniorstudents/', createseniorstudent_view, name='seniorstudents'),
    path('activation/createseniorresults1/', createseniorresult1_view, name='seniorresult1'),
    path('activation/createseniorresults2&3/', createseniorresult2_view, name='seniorresult2'),

    # Annual Student Record 
    path('activation/createjuniorstudentsAnnual1a/', createjuniorstudentAnnual1a_view, name='juniorstudents1a'),
    path('activation/createjuniorstudentsAnnual1b/', createjuniorstudentAnnual1b_view, name='juniorstudents1b'),
    path('activation/createjuniorstudentsAnnual1c/', createjuniorstudentAnnual1c_view, name='juniorstudents1c'),
    path('activation/createjuniorstudentsAnnual2a/', createjuniorstudentAnnual2a_view, name='juniorstudents2a'),
    path('activation/createjuniorstudentsAnnual2b/', createjuniorstudentAnnual2b_view, name='juniorstudents2b'),
    path('activation/createjuniorstudentsAnnual3/', createjuniorstudentAnnual3_view, name='juniorstudents3'),
    path('activation/createjuniorAnnualresults1a/', createjuniorresultAnnual1a_view, name='juniorresult1a'),
    path('activation/createjuniorAnnualresults1b/', createjuniorresultAnnual1b_view, name='juniorresult1b'),
    path('activation/createjuniorAnnualresults1c/', createjuniorresultAnnual1c_view, name='juniorresult1c'),
    path('activation/createjuniorAnnualresults2a/', createjuniorresultAnnual2a_view, name='juniorresult2a'),
    path('activation/createjuniorAnnualresults2b/', createjuniorresultAnnual2b_view, name='juniorresult2b'),
    path('activation/createjuniorAnnualresults3/', createjuniorresultAnnual3_view, name='juniorresult3'),
    path('activation/createseniorAnnualstudents/', createseniorstudentAnnual_view, name='seniorstudents'),
    path('activation/createseniorAnnualresults1/', createseniorresultAnnual1_view, name='seniorresult1'),
    path('activation/createseniorAnnualresults2&3/', createseniorresultAnnual2_view, name='seniorresult2'),

    path('activation/pins/', createPin, name='Pin'),   
    path('<str:Classname>/<int:id>/',students_view, name='students'),
    path('<str:Classname>/result/',result_view, name='result'),
    path('<str:Classname>/<str:Name>/pdf',result_pdf_view, name='pdf'),
    
    
    ]