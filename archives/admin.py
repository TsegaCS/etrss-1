from django.contrib import admin
from archives.models import Archives

class ArchiveAdmin(admin.ModelAdmin):
    list_display = ('id', 'place_name', 'latitude', 'longitude', 'request_date', 'applicationField', 'orderType', 'productLevel')
    list_display_links = ('id','place_name',)
    list_filter = ('applicationField',)
    search_fields = ('place_name','latitude','longitude','request_date','applicationField','orderType','productLevel','satellite_source','cloud_cover',)
    # list_per_page = 

admin.site.register(Archives, ArchiveAdmin)