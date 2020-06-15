from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('archiverequest/', views.map ,name='archives'),
    path('archiverequest/<int:id>/', views.map ,name='archives')    
]
