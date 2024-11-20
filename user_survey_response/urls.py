from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.user_survey_response, name='user_survey_response'),
]