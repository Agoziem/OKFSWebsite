from django.urls import path
from .views import (
    ebookdetail_view,
	category_view,
	ebooklist_view,
)

app_name = 'Elibrary'
urlpatterns = [
    path('', category_view, name='subjects'),
    path('<int:cate>/',ebooklist_view, name='ebooklist'),
    path('<int:id>/detail/',ebookdetail_view, name='ebookdetail'),
    
    ]