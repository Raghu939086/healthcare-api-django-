from django.db import models
from django.contrib.auth.models import User

# Patient Model
class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # record creator
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name


# Doctor Model
class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # record creator
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name


# Mapping Model (Assign Doctor to Patient)
class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='mappings')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='mappings')
    assigned_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.name} → {self.doctor.name}"
