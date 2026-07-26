from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientDetailsViewSet

# Initialize the DefaultRouter
router = DefaultRouter()
# Register the viewset with the 'patients' prefix
router.register(r'patients', PatientDetailsViewSet, basename='patient')

urlpatterns = [
    path('', include(router.urls)),
]