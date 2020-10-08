from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('mailGun', views.mailGun, name='mailGun'),
    path('login', views.login ,name='login'),
    path('register', views.register ,name='register'),
    path('logout', views.logout ,name='logout'),
]
