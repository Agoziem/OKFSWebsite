from django.urls import path
from django.conf.urls import url
from .views import (
    classes_view,
	students_view,
	result_view,
	activation_view,
	result_pdf_view,
	createjuniorstudent1a_view,
    createjuniorstudent1b_view,
    createjuniorstudent1c_view,
    createjuniorstudent2a_view,
    createjuniorstudent2b_view,
    createjuniorstudent3_view,
	createjuniorresult1a_view,
    createjuniorresult1b_view,
    createjuniorresult1c_view,
    createjuniorresult2a_view,
    createjuniorresult2b_view,
    createjuniorresult3_view,
	createseniorstudent_view,
	createseniorresult1_view,
    createseniorresult2_view,
	createPin,
)

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
    path('activation/createjuniorresults1/', createjuniorresult1a_view, name='juniorresult1a'),
    path('activation/createjuniorresults1/', createjuniorresult1b_view, name='juniorresult1b'),
    path('activation/createjuniorresults1/', createjuniorresult1c_view, name='juniorresult1c'),
    path('activation/createjuniorresults2a/', createjuniorresult2a_view, name='juniorresult2a'),
    path('activation/createjuniorresults2b/', createjuniorresult2b_view, name='juniorresult2b'),
    path('activation/createjuniorresults3/', createjuniorresult3_view, name='juniorresult3'),
    path('activation/createseniorstudents/', createseniorstudent_view, name='seniorstudents'),
    path('activation/createseniorresults1/', createseniorresult1_view, name='seniorresult1'),
    path('activation/createseniorresults2&3/', createseniorresult2_view, name='seniorresult2'),
    path('activation/pins/', createPin, name='Pin'),   
    path('<str:Classname>/',students_view, name='students'),
    path('<str:Classname>/result/',result_view, name='result'),
    path('<str:Classname>/<str:Name>/pdf',result_pdf_view, name='pdf'),
    
    
    ]