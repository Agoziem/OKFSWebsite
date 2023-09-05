from django.urls import path
from .views import initiate_payment,verify_payment

app_name = 'Payments'
urlpatterns = [
	path('',initiate_payment , name='initiate_payment'),
	path('<str:ref>/',verify_payment , name='verify_payment'),
    ]
