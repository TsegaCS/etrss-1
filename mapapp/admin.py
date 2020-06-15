from django.contrib import admin
from . models import latlng

class MapappAdmin(admin.ModelAdmin):
    list_display = ('id', 'organization', 'contact_person', 'latitude', 'longitude', 'request_date', 'applicationField', 'orderType', 'productLevel','satellite_source','cloud_cover',)
    list_display_links = ('id','organization','contact_person')
    # list_filter = ('applicationField',)
    search_fields = ('organization','contact_person','latitude','longitude','request_date','applicationField','orderType','productLevel','satellite_source','cloud_cover',)
    # list_per_page = 


admin.site.register(latlng, MapappAdmin)