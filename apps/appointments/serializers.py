from rest_framework import serializers
from django.db import transaction
from .models import Appointment
from apps.doctors.models import TimeSlotDoctor
from apps.users.models import PatientProfile

class AppointmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'timeslot']

    def validate_timeslot(self, timeslot):

        if not timeslot.is_available:
            raise serializers.ValidationError(
                "Bu TimeSlot allaqachon band qilingan"
            )
        return timeslot

    @transaction.atomic
    def create(self, validated_data):
        request = self.context['request']

        patient = PatientProfile.objects.filter(
            user=request.user
        ).first()

        if not patient:
            raise serializers.ValidationError(
                "Faqat patient appointment qila oladi"
            )

 
        timeslot = TimeSlotDoctor.objects.select_for_update().get(
            id=validated_data['timeslot'].id
        )

        if not timeslot.is_available:
            raise serializers.ValidationError(
                "Bu TimeSlot allaqachon band qilingan"
            )

        appointment = Appointment.objects.create(
            doctor=timeslot.doctor,
            patient=patient,
            timeslot=timeslot,
            status='confirmed'
        )

        timeslot.is_available = False
        timeslot.save()

        return appointment
