from django.contrib import admin

from . models import UserProfile

class AccountAdmin(admin.ModelAdmin):
    list_display = ('username','organization','country','city','department','is_staff','email','address','phone',)
    list_display_links = ('username','organization', 'email', 'phone')
    list_filter = ('country', 'organization',)
    search_fields = ('username','organization','country','city', 'department','email','address','phone')

admin.site.register(UserProfile, AccountAdmin)