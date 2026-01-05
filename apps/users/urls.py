from django.urls import path
from .views import RegisterView, LoginView, ProfileView, LogoutView, UsersListView, userDetailView, PatientProfileView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('me/', ProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('users/', UsersListView.as_view(), name='users_list'),
    path("users/<int:pk>/", userDetailView.as_view(), name="user_detail"),

    path("patient/profiles/", PatientProfileView.as_view(), name="patient_profile"),


    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

