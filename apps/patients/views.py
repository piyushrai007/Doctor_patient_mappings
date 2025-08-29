# apps/patients/views.py
from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Patient
from .serializers import PatientSerializer
from common.permissions import IsOwnerForPatients

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerForPatients]
    def get_queryset(self):
        return Patient.objects.filter(created_by=self.request.user).select_related("created_by")
    def perform_destroy(self, instance):
        if instance.created_by_id != self.request.user.id:
            raise PermissionDenied("Not owner")
        instance.delete()
