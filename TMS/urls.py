from django.urls import path
from .views import teachers_view

app_name = 'TMS'
urlpatterns = [
    path('',teachers_view, name='teachers'),
    ]