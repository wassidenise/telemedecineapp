from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='telemedicine-home'),
    path('about/', views.about, name='telemedicine-about'),
    path('contact/', views.contact, name='telemedicine-contact'),
    path('patientlist/', views.patientlist, name='telemedicine-patientlist'),
    path('appointment_scheduling/', views.appointment_scheduling, name='telemedicine-appointment_scheduling')

]
