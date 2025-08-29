# apps/mappings/models.py
from django.db import models
from apps.patients.models import Patient
from apps.doctors.models import Doctor

class PatientDoctor(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="doctor_links")
    doctor  = models.ForeignKey(Doctor,  on_delete=models.CASCADE, related_name="patient_links")
    assigned_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ("patient","doctor")
        ordering = ["-assigned_at"]
