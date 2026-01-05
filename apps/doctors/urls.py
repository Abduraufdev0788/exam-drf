from django.urls import path

from .views import DoctorsView, DoctorDetailView, TimeSlotsView

urlpatterns = [
    path('doctors/', DoctorsView.as_view(), name="doctors_list"),
    path('doctors/<int:doctor_id>/', DoctorDetailView.as_view(), name="doctor_detail"),
    path('doctors/<int:doctor_id>/timeslots/', TimeSlotsView.as_view(), name="doctor_timeslots"),
]

