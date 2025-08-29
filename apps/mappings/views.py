# apps/mappings/views.py
from rest_framework import generics, permissions, mixins, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import PatientDoctor
from .serializers import PatientDoctorSerializer, DoctorsForPatientSerializer
from apps.patients.models import Patient

class PatientDoctorViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin):
    queryset = PatientDoctor.objects.select_related("patient","doctor")
    serializer_class = PatientDoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=["get"], url_path=r"patient/(?P<patient_id>\d+)")
    def by_patient(self, request, patient_id=None):
        qs = self.get_queryset().filter(patient_id=patient_id)
        serializer = DoctorsForPatientSerializer(qs, many=True)
        return Response(serializer.data)
