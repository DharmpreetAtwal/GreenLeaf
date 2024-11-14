from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_tickets_view, name='user_tickets_view'),
]
