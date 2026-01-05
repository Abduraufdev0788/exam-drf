from rest_framework import serializers
from .models import DoctorProfile, TimeSlotDoctor

class DoctorProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = DoctorProfile
        fields = ['id', 'username', 'specialization', 'experience_years', 'gender']


class TimeSlotDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlotDoctor
        fields = '__all__'