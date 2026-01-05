from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.users.models import CustomUser, PatientProfile
from apps.doctors.models import DoctorProfile


@receiver(post_save, sender=CustomUser)
def create_profiles(sender, instance, created, **kwargs):
    if not created:
        return

    if instance.role == 'doctor':
        DoctorProfile.objects.create(
            user=instance,
            specialization='Unknown',
            experience_years=0,
            gender='male'
        )

    elif instance.role == 'patient':
        PatientProfile.objects.create(
            user=instance,
            phone='',
            date_of_birth='2000-01-01',
            gender='male'
        )
