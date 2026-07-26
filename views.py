from rest_framework import viewsets
from .models import PatientDetails
from .serializers import PatientDetailsSerializer

class PatientDetailsViewSet(viewsets.ModelViewSet):
    queryset = PatientDetails.objects.all()
    serializer_class = PatientDetailsSerializer