from django.shortcuts import redirect
from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dash, name='admin_dash'),
]
