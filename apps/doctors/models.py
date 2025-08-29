# apps/doctors/models.py
from django.db import models

class Doctor(models.Model):
    first_name = models.CharField(max_length=100, db_index=True)
    last_name  = models.CharField(max_length=100, db_index=True)
    specialization = models.CharField(max_length=120, db_index=True)
    phone = models.CharField(max_length=20, blank=True)
    hospital = models.CharField(max_length=150, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        indexes = [models.Index(fields=["specialization","last_name"])]
        ordering = ["-created_at"]
    def __str__(self): return f"Dr. {self.first_name} {self.last_name}"
