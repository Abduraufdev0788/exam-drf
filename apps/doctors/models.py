from django.db import models
from apps.users.models import CustomUser

class DoctorProfile(models.Model):
    GENDER_CHOISE = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='doctor_profile'
    )
    specialization = models.CharField(max_length=100)
    experience_years = models.PositiveIntegerField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOISE)