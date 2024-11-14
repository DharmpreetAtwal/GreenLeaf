from django.shortcuts import redirect
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_survey_response, name='user_survey_response'),
]
