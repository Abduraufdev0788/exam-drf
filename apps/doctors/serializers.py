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

    def validate(self, data):
        request = self.context['request']
        doctor = request.user.doctor_profile

        start_time = data.get('start_time')
        end_time = data.get('end_time')


        if start_time >= end_time:
            raise serializers.ValidationError(
                "Tugash vaqti boshlanish vaqtidan katta bo'lishi kerak"
            )


        overlap_exists = TimeSlotDoctor.objects.filter(
            doctor=doctor,
            start_time__lt=end_time,
            end_time__gt=start_time
        ).exists()

        if overlap_exists:
            raise serializers.ValidationError(
                "Bu vaqt oraligida boshqa TimeSlot mavjud"
            )

        return data