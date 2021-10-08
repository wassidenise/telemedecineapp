from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .models import patients



# Dummy data
posts = [
    {
        'name': 'John Doe',
        'age': '19',
        'sex': 'Male',
        'last_visit': 'January 1, 2021'
    },
    {
        'name': 'Jane Doe',
        'age': '20',
        'sex': 'Female',
        'last_visit': 'April 1, 2021'
    }
]



# Handles traffic to our homepage
def home(request):

    if request.method=='POST':
        ssn = request.POST['ssn']
        lastname = request.POST['lastname']
        firstname = request.POST['firstname']
        middlename = request.POST['middlename']
        dob = request.POST['dob']
        gender = request.POST['gender']
        height = request.POST['height']
        weight = request.POST['weight']
        address1 = request.POST['address1']
        city = request.POST['city']
        zipcode = request.POST['zipcode']
        state = request.POST['state']

        obj=patients()
        obj.ssn=ssn
        obj.lastname=lastname
        obj.firstname=firstname
        obj.middlename=middlename
        obj.dob=dob
        obj.gender=gender
        obj.height = height
        obj.weight = weight
        obj.address1 = address1
        obj.city = city
        obj.zipcode = zipcode
        obj.state = state
        obj.save()
    context = {

    }
    return render(request, 'telemedicine/home.html', context)


def about(request):
    context = {
        'posts': posts
    }
    return render(request, 'telemedicine/about.html', {'title': 'About'})

def patientlist(request):
    context = {
        'patients': patients.objects.all()  # Queries data from our database
    }
    return render(request,'telemedicine/patientlist.html', context)


def contact(request):
    return render(request, 'telemedicine/contact.html')


def patient(request):
    return render(request, 'telemedicine/about.html')


def physician(request):
    return render(request, 'telemedicine/about.html')
