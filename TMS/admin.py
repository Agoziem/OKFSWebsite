from django.contrib import admin
from.models import Teacher

# admin.site.register()
@admin.register(Teacher)
class AnnualStudentAdmin(admin.ModelAdmin):
    list_display=('Name','Subject')
    ordering=('Name',)
    search_fields=('Name','Subject',"Role")
    list_filter=('Subject',"Role")
