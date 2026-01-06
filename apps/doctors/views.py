from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.filters import SearchFilter
from rest_framework.exceptions import ValidationError

from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404


from apps.users.permissions import IsAdmin, IsPatient, IsDoctor
from .models import DoctorProfile, TimeSlotDoctor
from .serializers import DoctorProfileSerializer, TimeSlotDoctorSerializer

class DoctorsView(ListAPIView):
    permission_classes = [IsAuthenticated, IsAdmin | IsPatient]
    serializer_class = DoctorProfileSerializer
    queryset = DoctorProfile.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['specialization', 'user__first_name', 'user__last_name', 'user__username']


class DoctorDetailView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin | IsPatient]

    def get(self, request:Request, doctor_id:int):
        doctor = DoctorProfile.objects.get(id = doctor_id)
        serializer = DoctorProfileSerializer(doctor)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class TimeSlotsView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin | IsPatient]

    def get(self, request:Request, doctor_id:int):
        doctor = DoctorProfile.objects.get(id = doctor_id)
        time_slots = TimeSlotDoctor.objects.filter(doctor=doctor)
        serializer = TimeSlotDoctorSerializer(time_slots, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class DoctorProfileView(APIView):
    permission_classes = [IsAuthenticated, IsDoctor]
    def get(self, request:Request):
        doctor = DoctorProfile.objects.get(user=request.user)
        serializer = DoctorProfileSerializer(doctor)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def patch(self, request:Request):
        doctor = DoctorProfile.objects.get(user=request.user)
        serializer = DoctorProfileSerializer(doctor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TimeSlotCreateView(APIView):
    permission_classes = [IsAuthenticated, IsDoctor]

    def get(self, request:Request):
        doctor = DoctorProfile.objects.filter(user=request.user).first()
        timeslots = TimeSlotDoctor.objects.filter(doctor=doctor)
        serializer = TimeSlotDoctorSerializer(timeslots, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request:Request):
        doctor = DoctorProfile.objects.filter(user=request.user).first()
        data = request.data.copy()
        data['doctor'] = doctor.id
        serializer = TimeSlotDoctorSerializer(data=data, context={'request': request} )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class TimeSlotDetailView(APIView):
    permission_classes = [IsAuthenticated, IsDoctor]

    def get(self, request:Request, slot_id:int):
        timeslot = get_object_or_404(TimeSlotDoctor, id = slot_id, doctor = request.user.doctor_profile)
        serializer = TimeSlotDoctorSerializer(timeslot)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request:Request, slot_id:int):
        timeslot = get_object_or_404(TimeSlotDoctor, id = slot_id, doctor = request.user.doctor_profile)
        if not timeslot.is_available:
            raise ValidationError(
                "Band qilingan TimeSlotni o'chirish mumkin emas"
            )
        timeslot.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
