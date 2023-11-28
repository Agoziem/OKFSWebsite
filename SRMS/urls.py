from django.urls import path
from django.conf.urls import url
from .views import *
app_name = 'SRMS'
urlpatterns = [
    path('', classes_view, name='classes'),
    path('<str:Classname>/', get_Students, name='get_students'),
    ]