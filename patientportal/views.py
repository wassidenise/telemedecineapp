from django.contrib.auth.decorators import login_required


from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import PatientRegisterForm


from django.shortcuts import render

def register(request):
    if request.method == 'POST':
        form = PatientRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}, please log in.')
            return redirect('login')
    else:
        form = PatientRegisterForm()
    return render(request, 'patientportal/register.html', {'form': form})


@login_required
def patientportalhome(request):
    return render(request, 'patientportal/patientportalhome.html')


@login_required
def patientprofile(request):
    return render(request, 'patientportal/patientprofile.html')