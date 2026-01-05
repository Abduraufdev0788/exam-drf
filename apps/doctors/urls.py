from django.urls import path

from .views import DoctorsView, DoctorDetailView

urlpatterns = [
    path('doctors/', DoctorsView.as_view(), name="doctors_list"),
    path('doctors/<int:doctor_id>/', DoctorDetailView.as_view(), name="doctor_detail"),
]

