from django.urls import path
from django.conf.urls import url
from .views import *
app_name = 'SRMS'
urlpatterns = [
    path('', classes_view, name='classes'),
    path('activation/', activation_view, name='activation'),

# TERMLY RESULT

# Junior Termly Details Url //////////////////////////////////////////////////////////
    path('activation/createjuniorstudents1a/', createjuniorstudent1a_view, name='juniorstudents1a'),
    path('activation/createjuniorstudents1b/', createjuniorstudent1b_view, name='juniorstudents1b'),
    path('activation/createjuniorstudents1c/', createjuniorstudent1c_view, name='juniorstudents1c'),

    path('activation/createjuniorstudents2a/', createjuniorstudent2a_view, name='juniorstudents2a'),
    path('activation/createjuniorstudents2b/', createjuniorstudent2b_view, name='juniorstudents2b'),
    path('activation/createjuniorstudents2c/', createjuniorstudent2c_view, name='juniorstudents2c'),

    path('activation/createjuniorstudents3a/', createjuniorstudent3a_view, name='juniorstudents3a'),
    path('activation/createjuniorstudents3b/', createjuniorstudent3b_view, name='juniorstudents3b'),

# Junior Termly Result Url //////////////////////////////////////////////////////////
    path('activation/createjuniorresults1a/', createjuniorresult1a_view, name='juniorresult1a'),
    path('activation/createjuniorresults1b/', createjuniorresult1b_view, name='juniorresult1b'),
    path('activation/createjuniorresults1c/', createjuniorresult1c_view, name='juniorresult1c'),

    path('activation/createjuniorresults2a/', createjuniorresult2a_view, name='juniorresult2a'),
    path('activation/createjuniorresults2b/', createjuniorresult2b_view, name='juniorresult2b'),
    path('activation/createjuniorresults2c/', createjuniorresult2c_view, name='juniorresult2c'),

    path('activation/createjuniorresults3a/', createjuniorresult3a_view, name='juniorresult3a'),
    path('activation/createjuniorresults3b/', createjuniorresult3b_view, name='juniorresult3b'),

# ANNUAL RESULT

# Junior Annual Details Url //////////////////////////////////////////////////////////
    path('activation/createjuniorstudentsAnnual1a/', createjuniorstudentAnnual1a_view, name='juniorstudentsannual1a'),
    path('activation/createjuniorstudentsAnnual1b/', createjuniorstudentAnnual1b_view, name='juniorstudentsannual1b'),
    path('activation/createjuniorstudentsAnnual1c/', createjuniorstudentAnnual1c_view, name='juniorstudentsannual1c'),

    path('activation/createjuniorstudentsAnnual2a/', createjuniorstudentAnnual2a_view, name='juniorstudentsannual2a'),
    path('activation/createjuniorstudentsAnnual2b/', createjuniorstudentAnnual2b_view, name='juniorstudentsannual2b'),
    path('activation/createjuniorstudentsAnnual2b/', createjuniorstudentAnnual2c_view, name='juniorstudentsannual2c'),

    path('activation/createjuniorstudentsAnnual3a/', createjuniorstudentAnnual3a_view, name='juniorstudentsannual3a'),
    path('activation/createjuniorstudentsAnnual3b/', createjuniorstudentAnnual3b_view, name='juniorstudentsannual3b'),

# Junior Annual Result Url //////////////////////////////////////////////////////////
    path('activation/createjuniorAnnualresults1a/', createjuniorresultAnnual1a_view, name='juniorresultannual1a'),
    path('activation/createjuniorAnnualresults1b/', createjuniorresultAnnual1b_view, name='juniorresultannual1b'),
    path('activation/createjuniorAnnualresults1c/', createjuniorresultAnnual1c_view, name='juniorresultannual1c'),

    path('activation/createjuniorAnnualresults2a/', createjuniorresultAnnual2a_view, name='juniorresultannual2a'),
    path('activation/createjuniorAnnualresults2b/', createjuniorresultAnnual2b_view, name='juniorresultannual2b'),
    path('activation/createjuniorAnnualresults2b/', createjuniorresultAnnual2c_view, name='juniorresultannual2c'),


    path('activation/createjuniorAnnualresults3/', createjuniorresultAnnual3a_view, name='juniorresultannual3a'),
    path('activation/createjuniorAnnualresults3/', createjuniorresultAnnual3b_view, name='juniorresultannual3b'),


# TERMLY RESULT

# senior Termly Details Url //////////////////////////////////////////////////////////
    path('activation/createseniorstudents1/', createseniorstudent1_view, name='seniorstudents1'),

    path('activation/createseniorstudents2/', createseniorstudent2_view, name='seniorstudents2'),

    path('activation/createseniorstudents3/', createseniorstudent3_view, name='seniorstudents3'),

# senior Termly result Url //////////////////////////////////////////////////////////
    path('activation/createseniorresults1/', createseniorresult1_view, name='seniorresult1'),

    path('activation/createseniorresults2a/', createseniorresult2a_view, name='seniorresult2a'),
    path('activation/createseniorresults2b/', createseniorresult2b_view, name='seniorresult2b'),

    path('activation/createseniorresults3a/', createseniorresult3a_view, name='seniorresult3a'),
    path('activation/createseniorresults3b/', createseniorresult3b_view, name='seniorresult3b'),

# ANNUAL RESULT 

# Senior Annual Details Url //////////////////////////////////////////////////////////
    path('activation/createseniorAnnualstudents1/', createseniorstudentAnnual1_view, name='seniorstudentsannual1'),

    path('activation/createseniorAnnualstudents2/', createseniorstudentAnnual2_view, name='seniorstudentsannual2'),

    path('activation/createseniorAnnualstudents3/', createseniorstudentAnnual3_view, name='seniorstudentsannual3'),

# Senior Annual Result Url //////////////////////////////////////////////////////////
    path('activation/createseniorAnnualresults1/', createseniorresultAnnual1_view, name='seniorresultannual1'),

    path('activation/createseniorAnnualresults2a/', createseniorresultAnnual2a_view, name='seniorresultannual2a'),
    path('activation/createseniorAnnualresults2b/', createseniorresultAnnual2b_view, name='seniorresultannual2b'),

    path('activation/createseniorAnnualresults3a/', createseniorresultAnnual3a_view, name='seniorresultannual3a'),
    path('activation/createseniorAnnualresults3b/', createseniorresultAnnual3b_view, name='seniorresultannual3b'),

    path('activation/pins/', createPin, name='Pin'),   
    path('<str:Classname>/<int:id>/',students_view, name='students'),
    path('<str:Classname>/result/',result_view, name='result'),
    path('<str:Classname>/<str:Name>/pdf',result_pdf_view, name='pdf'),
    
    
    ]