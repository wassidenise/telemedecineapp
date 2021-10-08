"""djangoProjectTelemedicine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('telemedicine/', include('telemedicine.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from patientportal import views as patientportal_views
from physicianportal import views as physicianportal_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', patientportal_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='patientportal/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='patientportal/logout.html'), name='logout'),
    path('patientportal/', patientportal_views.patientportalhome, name='patientportalhome'),
    path('patientprofile/', patientportal_views.patientprofile, name='patientprofile'),
    path('', include('telemedicine.urls')),  # Empty path makes this our homepage
]
