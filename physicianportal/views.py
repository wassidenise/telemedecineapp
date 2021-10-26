from django.contrib.auth.decorators import login_required


from django.shortcuts import render, redirect
from django.contrib import messages


from django.shortcuts import render

@login_required
def patientportalhome(request):
    return render(request, 'patientportal/patientportalhome.html')


@login_required
def patientprofile(request):
    return render(request, 'patientportal/patientprofile.html')

