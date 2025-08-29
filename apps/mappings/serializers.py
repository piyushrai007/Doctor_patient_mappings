# apps/mappings/serializers.py
from rest_framework import serializers
from .models import PatientDoctor
from apps.doctors.serializers import DoctorSerializer

class PatientDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDoctor
        fields = ("id","patient","doctor","assigned_at")
        read_only_fields = ("assigned_at",)

class DoctorsForPatientSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only=True)
    class Meta:
        model = PatientDoctor
        fields = ("id","doctor","assigned_at")
