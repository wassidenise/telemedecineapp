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
    id = models.PositiveIntegerField(primary_key=True)
    ssn = models.PositiveIntegerField()
    dob = models.DateField()
    height = models.FloatField()
    gender = models.CharField(max_length=1)
    ethnicity = models.CharField(max_length=20, blank=True, null=True)
    job = models.CharField(max_length=50, blank=True, null=True)
    smoking = models.BooleanField(blank=True, null=True)
    familyhistory = models.TextField(blank=True, null=True)
    address1 = models.CharField(max_length=50, blank=True, null=True)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(max_length=2, blank=True, null=True)
    weight = models.FloatField()



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
    aptdatetime=models.DateTimeField()

class visits(models.Model):
    appointmentno=models.ForeignKey(appointments, on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField(default=00)
    symptom=models.TextField(max_length=200)
    condition=models.TextField(max_length=200)
    notes=models.TextField(max_length=500)
    followupbool=models.BooleanField(default=False)

class recordings(models.Model):
    visitno=models.ForeignKey(visits, on_delete=models.CASCADE)
    videoURL=models.URLField()
    messageURL=models.URLField()

class slots(models.Model):
    id = models.PositiveIntegerField(null=False, primary_key=True)
    start_time = models.TextField()
    end_time = models.TextField()

class appointment_date(models.Model):
    id = models.PositiveIntegerField(null=False, primary_key=True)
    date = models.DateField(blank=True, null=True)
    timeslot_id = models.IntegerField(blank=True, null=True)
    taken = models.BooleanField(blank=True, null=True)

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(db_column='middle name', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    phone = models.IntegerField(blank=True, null=True)








