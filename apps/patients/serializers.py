# apps/patients/serializers.py
from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ("id","first_name","last_name","dob","gender","phone","created_at","updated_at")
        read_only_fields = ("created_at","updated_at")
    def create(self, validated):
        validated["created_by"] = self.context["request"].user
        return super().create(validated)
