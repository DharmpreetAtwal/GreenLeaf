from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_surveys, name='user_surveys'),
]
