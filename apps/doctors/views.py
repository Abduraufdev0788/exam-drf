from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.filters import SearchFilter

from rest_framework.permissions import IsAuthenticated


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
    

class TimeSlotCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsDoctor]
    serializer_class = TimeSlotDoctorSerializer

    def get_queryset(self):
        return TimeSlotDoctor.objects.filter(doctor=self.request.user.doctor_profile)

    def perform_create(self, serializer):
        serializer.save(doctor=self.request.user.doctor_profile)
        
        
