from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homes'),
    path('request/', views.map ,name='map')
]
