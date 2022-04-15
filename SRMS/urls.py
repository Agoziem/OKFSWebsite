from django.urls import path
from django.conf.urls import url
from .views import (
    classes_view,
	students_view,
	result_view,
	activation_view,
	result_pdf_view,
	createjuniorstudent_view,
	createjuniorresult_view,
	createseniorstudent_view,
	createseniorresult1_view,
    createseniorresult2_view,
	createPin,
)

app_name = 'SRMS'
urlpatterns = [
    path('', classes_view, name='classes'),
    path('activation/', activation_view, name='activation'),
    path('activation/createjuniorstudents/', createjuniorstudent_view, name='juniorstudents'),
    path('activation/createjuniorresults/', createjuniorresult_view, name='juniorresult'),
    path('activation/createseniorstudents/', createseniorstudent_view, name='seniorstudents'),
    path('activation/createseniorresults1/', createseniorresult1_view, name='seniorresult1'),
    path('activation/createseniorresults2&3/', createseniorresult2_view, name='seniorresult2'),
    path('activation/pins/', createPin, name='Pin'),   
    path('<str:Classname>/',students_view, name='students'),
    path('<str:Classname>/result/',result_view, name='result'),
    path('<str:Classname>/<str:Name>/pdf',result_pdf_view, name='pdf'),
    
    
    ]