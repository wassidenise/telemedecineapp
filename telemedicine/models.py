from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):  # Each class will be its own table in the database
    name = models.CharField(max_length=100)
    doctor = models.TextField()
    date_last_visit = models.DateTimeField(default=timezone.now)
    current_medications = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class patients(models.Model):
    ssn=models.PositiveIntegerField(null=False)
    lastname= models.CharField(max_length=50, null=False)
    firstname = models.CharField(max_length=50, null=False)
    middlename = models.CharField(max_length=50, null=False)
    dob=models.DateField(null=False)
    height=models.FloatField(max_length=4, null=False)
    weight = models.FloatField(max_length=4, null=False)
    gender=models.CharField(max_length=1,choices=(('f', 'female'),('m','male')))
    ethnicity=models.CharField(max_length=20, null=True)
    job=models.CharField(max_length=50, null=True)
    smoking=models.BooleanField(default=False,null=True)
    familyhistory=models.TextField( null=True)
    address1=models.CharField(max_length=50, null=True)
    address2 = models.CharField(max_length=50, null=True)
    city=models.CharField(max_length=50)
    zipcode=models.IntegerField()
    state=models.CharField(max_length=2, null=True)
    phone=models.PositiveIntegerField(max_length=10, null=True)



class immunizations(models.Model):
    patientno=models.ForeignKey(patients, on_delete=models.CASCADE)
    immunizations=models.TextField(max_length=200)
    dateimmunization=models.DateField()


class medicationsallergies(models.Model):
    patientno=models.ForeignKey(patients, on_delete=models.CASCADE)
    medications=models.TextField(max_length=200)
    enddatemedications=models.DateField()
    allergies=models.TextField(max_length=200)

class prescriptions(models.Model):
    patientno=models.ForeignKey(patients, on_delete=models.CASCADE)
    medicinename=models.TextField(max_length=200)
    dosage=models.CharField(max_length=200)
    startdate = models.DateField()
    enddate=models.DateField()

class chartreports(models.Model):
    patientno=models.ForeignKey(patients, on_delete=models.CASCADE)
    filename=models.CharField(max_length=50)
    notes=models.TextField(max_length=250)
    fileurl=models.URLField()
    date=models.DateField()

class appointments(models.Model):
    patientno=models.ForeignKey(patients, on_delete=models.CASCADE)
    madeon=models.DateField()
    drname=models.CharField(max_length=200)
    aptdatetime=models.DateTimeField()

class visits(models.Model):
    appointmentno=models.ForeignKey(appointments, on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()
    symptom=models.TextField(max_length=200)
    condition=models.TextField(max_length=200)
    notes=models.TextField(max_length=500)
    followupbool=models.BooleanField(default=False)

class recordings(models.Model):
    visitno=models.ForeignKey(visits, on_delete=models.CASCADE)
    videoURL=models.URLField()
    messageURL=models.URLField()







