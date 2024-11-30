from django.urls import path
from .views import *

urlpatterns = [
    # CustomUser URLs
    path('users/', CustomUserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', CustomUserDetailView.as_view(), name='user_detail'),
    path('users/create/', CustomUserCreateView.as_view(), name='user_create'),
    path('users/<int:pk>/update/', CustomUserUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/delete/', CustomUserDeleteView.as_view(), name='user_delete'),

    # Role URLs
    path('roles/', RoleListView.as_view(), name='role_list'),
    path('roles/<int:pk>/', RoleDetailView.as_view(), name='role_detail'),
    path('roles/create/', RoleCreateView.as_view(), name='role_create'),
    path('roles/<int:pk>/update/', RoleUpdateView.as_view(), name='role_update'),
    path('roles/<int:pk>/delete/', RoleDeleteView.as_view(), name='role_delete'),

    # Profile URLs
    path('profiles/', ProfileListView.as_view(), name='profile_list'),
    path('profiles/<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('profiles/create/', ProfileCreateView.as_view(), name='profile_create'),
    path('profiles/<int:pk>/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('profiles/<int:pk>/delete/', ProfileDeleteView.as_view(), name='profile_delete'),
    
    path('specialities/', SpecialityListView.as_view(), name='speciality_list'),
    path('specialities/<int:pk>/', SpecialityDetailView.as_view(), name='speciality_detail'),
    path('specialities/create/', SpecialityCreateView.as_view(), name='speciality_create'),
    path('specialities/<int:pk>/update/', SpecialityUpdateView.as_view(), name='speciality_update'),
    path('specialities/<int:pk>/delete/', SpecialityDeleteView.as_view(), name='speciality_delete'),
    
    path('diagnoses/', DiagnozeListView.as_view(), name='diagnoze_list'),
    path('diagnoses/<int:pk>/', DiagnozeDetailView.as_view(), name='diagnoze_detail'),
    path('diagnoses/create/', DiagnozeCreateView.as_view(), name='diagnoze_create'),
    path('diagnoses/<int:pk>/update/', DiagnozeUpdateView.as_view(), name='diagnoze_update'),
    path('diagnoses/<int:pk>/delete/', DiagnozeDeleteView.as_view(), name='diagnoze_delete'),

    # TimeTable URLs
    path('timetables/', TimeTableListView.as_view(), name='timetable_list'),
    path('timetables/<int:pk>/', TimeTableDetailView.as_view(), name='timetable_detail'),
    path('timetables/create/', TimeTableCreateView.as_view(), name='timetable_create'),
    path('timetables/<int:pk>/update/', TimeTableUpdateView.as_view(), name='timetable_update'),
    path('timetables/<int:pk>/delete/', TimeTableDeleteView.as_view(), name='timetable_delete'),

    # Appointment URLs
    path('appointments/', AppointmentListView.as_view(), name='appointment_list'),
    path('appointments/<int:pk>/', AppointmentDetailView.as_view(), name='appointment_detail'),
    path('appointments/create/', AppointmentCreateView.as_view(), name='appointment_create'),
    path('appointments/<int:pk>/update/', AppointmentUpdateView.as_view(), name='appointment_update'),
    path('appointments/<int:pk>/delete/', AppointmentDeleteView.as_view(), name='appointment_delete'),
]
