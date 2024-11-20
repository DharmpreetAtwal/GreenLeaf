"""
URL configuration for GreenLeaf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('admin_dash/', permanent=False)),
    path('admin_dash/', include('admin_dash.urls')),
    path('user_survey_response/', include('user_survey_response.urls')),
    path('user_surveys/', include('user_surveys.urls')),
    path('user_tickets/', include('user_tickets.urls')),
    path('admin/', admin.site.urls),
]
