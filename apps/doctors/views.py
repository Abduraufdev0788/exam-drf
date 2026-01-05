from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated


from apps.users.permissions import IsAdmin, IsPatient
from .models import DoctorProfile, TimeSlotDoctor
from .serializers import DoctorProfileSerializer, TimeSlotDoctorSerializer

class DoctorsView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin | IsPatient]

    def get(self, request:Request):
        doctors = DoctorProfile.objects.all()
        serializer = DoctorProfileSerializer(doctors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


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
        
