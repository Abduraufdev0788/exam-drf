from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import AppointmentCreateSerializer

class AppointmentCreateView(CreateAPIView):
    serializer_class = AppointmentCreateSerializer
    permission_classes = [IsAuthenticated]
