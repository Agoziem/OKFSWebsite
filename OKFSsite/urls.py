
from django.contrib import admin
from home.views import *
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	path('', home_view, name='home'),
    path('about/',about_view, name='about'),
    path('gallery/', photo_gallery_view, name='gallery'),
    path('activate/',student_card_view, name='cardactivate'),

    path('teachers/', teachers_view, name='teachers'),
    path('home/', home2_view, name='home2'),
    path('contact/', contact_form, name='contact'),
    path('admin/', admin.site.urls),
    path('Elibrary/', include('Elibrary.urls')),
    path('SRMS/', include('SRMS.urls')),
    path('TMS/', include('TMS.urls')),
    path('Payments/', include('Payments.urls')),
    path('Admission/', include('Admission.urls')),
    path('Accounts/', include('Accounts.urls')),
]

if settings.DEBUG_ENV:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

admin.site.site_header='OKFS Awada'
admin.site.index_title='Site Administration'