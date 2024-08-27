from django.contrib import admin
from.models import *

admin.site.register(School)
admin.site.register(Subscription)
admin.site.register(Management)
admin.site.register(PhotoGallery)
admin.site.register(UpcomingEvents)
admin.site.register(FAQ)
admin.site.register(Contact)


@admin.register(CarouselItem)
class CarouselItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'cta_text')
    search_fields = ('title', 'cta_text')
    list_filter = ('title', 'cta_text')


@admin.register(SchoolDocument)
class SchoolDocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'document')
    search_fields = ('title', 'document')
    list_filter = ('title', 'document')
