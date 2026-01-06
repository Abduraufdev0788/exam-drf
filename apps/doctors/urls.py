from django.urls import path

from .views import DoctorsView, DoctorDetailView, TimeSlotsView, DoctorProfileView, TimeSlotCreateView, TimeSlotDetailView

urlpatterns = [
    path('doctors/', DoctorsView.as_view(), name="doctors_list"),
    path('doctors/<int:doctor_id>/', DoctorDetailView.as_view(), name="doctor_detail"),
    path('doctors/<int:doctor_id>/timeslots/', TimeSlotsView.as_view(), name="doctor_timeslots"),

    path('doctor/profile/', DoctorProfileView.as_view(), name='doctor_profile'),


    path('timeslots/',TimeSlotCreateView.as_view(), name="timeslots_view" ),
    path('timeslots/<int:slot_id>/', TimeSlotDetailView.as_view(), name = "timeslot_detail")
]

