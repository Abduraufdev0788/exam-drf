from django.db import models
from apps.doctors.models import DoctorProfile, TimeSlotDoctor
from apps.users.models import PatientProfile


class TimeSlot(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name='doctor_appointments')
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='patient_appointments')
    timeslot = models.OneToOneField(TimeSlotDoctor, on_delete=models.CASCADE, related_name='appointment')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}.{self.doctor} ----- {self.patient}"
