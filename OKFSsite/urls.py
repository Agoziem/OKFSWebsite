
from django.contrib import admin
from home.views import home_view,about_view,photo_gallery_view,home2_view,contact_form
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
	path('', home_view, name='home'),
    path('about/',about_view, name='about'),
    path('gallery/', photo_gallery_view, name='gallery'),
    path('home/', home2_view, name='home2'),
    path('contact/', contact_form, name='contact'),
    path('admin/', admin.site.urls),
    path('Elibrary/', include('Elibrary.urls')),
    path('SRMS/', include('SRMS.urls')),
    path('TMS/', include('TMS.urls')),
    path('Payments/', include('Payments.urls')),
    path('Admission/', include('Admission.urls')),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)