from django.urls import path
from .views import initiate_payment2,verify_payment2, admission_details,form_pdf_view

app_name = 'Admission'
urlpatterns = [
	path('',initiate_payment2, name='initiate_payment2'),
	path('details/', admission_details , name='details'),
	path('details/<int:id>/pdf', form_pdf_view, name='pdf'),
	path('<str:ref>/',verify_payment2, name='verify_payment2'),
    ]