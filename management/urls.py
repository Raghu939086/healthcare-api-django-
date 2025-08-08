from django.urls import path
from .views import (RegisterView,PatientListCreateView, PatientDetailView,DoctorListCreateView, DoctorDetailView,MappingListCreateView, MappingDetailView)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Auth
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Patients
    path('patients/', PatientListCreateView.as_view(), name='patients-list-create'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patients-detail'),

    # Doctors
    path('doctors/', DoctorListCreateView.as_view(), name='doctors-list-create'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctors-detail'),

    # Mappings
    path('mappings/', MappingListCreateView.as_view(), name='mappings-list-create'),
    path('mappings/<int:pk>/', MappingDetailView.as_view(), name='mappings-detail'),
]