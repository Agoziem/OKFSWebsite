from django.urls import path
from .views.adminviews import *
from .views.formteachersviews import *
from .views.Cbtviews import *
from .views.classteachersviews import *
from .views.views import *

app_name = 'TMS'
urlpatterns = [
    # Teachers views
	path('',Teachers_dashboard_view , name='Teachers_dashboard'),
	path('<int:id>/profile/', profile_view , name='profile'),
    
	# CBT views
	# path('<int:teachers_id>/CBT_questions/',CBT_Questions_view , name='CBT_Questions'),
	# path('<int:id>/CBT_update_details/',CBT_update_details , name='CBT_update_details'),
	# path('submit_questions/',submitquestion_view , name='Submit_questions'),

	# Form teachers views
	path('<str:Classname>/PublishResults/',PublishResults_view , name='PublishResults'),   
	path('getstudentsubjecttotals/',getstudentsubjecttotals_view , name='getstudentsubjecttotals'),   
	path('publishstudentresult/',publishstudentresult_view , name='publishstudentresult'),
	path('unpublishclassresult/',unpublish_classresults_view , name='unpublishstudentresult'),
    path('<str:Classname>/AnnualResults/',PublishAnnualResults_view , name='AnnualResults'), 
    path('annualclassresultcomputation/',annual_class_computation_view , name='annualclassresultcomputation'),
    path('publishannualclassresult/',publish_annualstudentresult_view , name='publishannualresult'),
    path('unpublishannualclassresult/',unpublish_annual_classresults_view , name='unpublishannualresult'),
    
	path('<str:Classname>/<int:session_id>/Students/',Students_view , name='Students'),   
	path('newStudent/', createstudent_view , name='createstudent'),   
	path('updateStudent/', updatestudent_view , name='updatestudent'),   
	path('DeleteStudents/', DeleteStudents_view , name='DeleteStudents'),   

    # Class Teachers Views
	path('<str:Classname>/<int:id>/result_computation/',result_computation_view , name='result_computation'),
	path('getstudentresults/',get_students_result_view , name='getstudentresults'),   
	path('updatestudentresults/',update_student_result_view , name='updatestudentresults'),   
	path('submitallstudentresult/',submitallstudentresult_view , name='submitallstudentresult'), 
    path('unpublishstudentresults/',unpublish_results_view , name='unpublishstudentresults'),
    path('<str:Classname>/<int:id>/annualresult_computation/',annualresult_computation , name='annualresult_computation'),
    path('annualresultcomputation/',annual_result_computation_view , name='annualresultcomputation'),
    path('publishannualresults/',publish_annual_results , name='publishannualresults'),
    path('unpublishannualresults/',unpublish_annual_results , name='unpublishannualresults'),

	# Admin urls
    path('schoolresults/',schoolresult_view , name='schoolresults'),
    path('getclasspublishedResults/',getclasspublishedResults , name='getclasspublishedResults'),
    path('schoolannualresult/',schoolannualresult_view, name='schoolannualresult'),
    path('getclassannualpublishedResults/',getclassannualpublishedResults, name='getclassannualpublishedResults'),
]