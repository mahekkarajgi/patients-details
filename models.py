

# Create your models here.
from django.db import models

# Create your models here.
class PatientDetails(models.Model):
    # Basic Information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(
        max_length=10, 
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
        blank=True, 
        null=True
    )
    
    # Contact Information
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    
    # Hospital/Medical Specifics
    medical_record_number = models.CharField(max_length=50, unique=True)
    room_number = models.CharField(max_length=20, blank=True, null=True)
    disease_description = models.TextField(blank=True, null=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} (MRN: {self.medical_record_number})"