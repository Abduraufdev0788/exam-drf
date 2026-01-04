from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE = (
        ('admin', 'Admin'),
        ('user', 'User'),
        ('doctor', 'Doctor'),
    )
    role = models.CharField(max_length=10, choices=ROLE, default='user')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    


class PatientProfile(models.Model):
    GENDER_CHOISE = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='patient_profile'
    )
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOISE)




    @property
    def is_admin(self)->bool:
        return self.role == self.role.admin
    
    @property
    def is_user(self)->bool:
        return self.role == self.role.user
    
    @property
    def is_doctor(self)->bool:
        return self.role == self.role.doctor
    