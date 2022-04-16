from django.urls import path
from django.conf.urls import url
from .views import (
    classes_view,
	students_view,
	result_view,
	activation_view,
	result_pdf_view,
	createjuniorstudent1_view,
    createjuniorstudent2_view,
    createjuniorstudent3_view,
	createjuniorresult1_view,
    createjuniorresult2_view,
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
    path('activation/createjuniorstudents1/', createjuniorstudent1_view, name='juniorstudents1'),
    path('activation/createjuniorstudents2/', createjuniorstudent2_view, name='juniorstudents2'),
    path('activation/createjuniorstudents3/', createjuniorstudent3_view, name='juniorstudents3'),
    path('activation/createjuniorresults1/', createjuniorresult1_view, name='juniorresult1'),
    path('activation/createjuniorresults2/', createjuniorresult2_view, name='juniorresult2'),
    path('activation/createjuniorresults3/', createjuniorresult3_view, name='juniorresult3'),
    path('activation/createseniorstudents/', createseniorstudent_view, name='seniorstudents'),
    path('activation/createseniorresults1/', createseniorresult1_view, name='seniorresult1'),
    path('activation/createseniorresults2&3/', createseniorresult2_view, name='seniorresult2'),
    path('activation/pins/', createPin, name='Pin'),   
    path('<str:Classname>/',students_view, name='students'),
    path('<str:Classname>/result/',result_view, name='result'),
    path('<str:Classname>/<str:Name>/pdf',result_pdf_view, name='pdf'),
    
    
    ]