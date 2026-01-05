from rest_framework import serializers
from .models import DoctorProfile, TimeSlotDoctor

class DoctorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = '__all__'


class TimeSlotDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlotDoctor
        fields = '__all__'