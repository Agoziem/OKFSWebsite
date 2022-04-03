from django.shortcuts import render
from .models import Teacher

def teachers_view(request):
	queryset= Teacher.objects.all()
	context = {
		"Teachers": queryset,
    }
	return render(request, "teachers_data.html", context)
	
	
