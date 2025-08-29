from django.db import models
from django.conf import settings

class Patient(models.Model):
    first_name = models.CharField(max_length=100, db_index=True)
    last_name  = models.CharField(max_length=100, db_index=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, choices=[("male","male"),("female","female"),("other","other")], blank=True)
    phone = models.CharField(max_length=20, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="patients")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        indexes = [models.Index(fields=["last_name","first_name"])]
        ordering = ["-created_at"]
    def __str__(self): return f"{self.first_name} {self.last_name}"
