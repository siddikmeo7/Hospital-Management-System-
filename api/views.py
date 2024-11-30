from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import CustomUser, Role, Profile, Speciality, Diagnoze, TimeTable, Appointment


# CustomUser Views
class CustomUserListView(ListView):
    model = CustomUser
    template_name = 'user_list.html'


class CustomUserDetailView(DetailView):
    model = CustomUser
    template_name = 'user_detail.html'


class CustomUserCreateView(CreateView):
    model = CustomUser
    fields = ['username', 'email', 'phone_number', 'role']
    template_name = 'user_form.html'
    success_url = reverse_lazy('user_list')


class CustomUserUpdateView(UpdateView):
    model = CustomUser
    fields = ['username', 'email', 'phone_number', 'role']
    template_name = 'user_form.html'
    success_url = reverse_lazy('user_list')


class CustomUserDeleteView(DeleteView):
    model = CustomUser
    template_name = 'user_confirm_delete.html'
    success_url = reverse_lazy('user_list')


# Role Views
class RoleListView(ListView):
    model = Role
    template_name = 'role_list.html'


class RoleDetailView(DetailView):
    model = Role
    template_name = 'role_detail.html'


class RoleCreateView(CreateView):
    model = Role
    fields = ['title']
    template_name = 'role_form.html'
    success_url = reverse_lazy('role_list')


class RoleUpdateView(UpdateView):
    model = Role
    fields = ['title']
    template_name = 'role_form.html'
    success_url = reverse_lazy('role_list')


class RoleDeleteView(DeleteView):
    model = Role
    template_name = 'role_confirm_delete.html'
    success_url = reverse_lazy('role_list')


# Profile Views
class ProfileListView(ListView):
    model = Profile
    template_name = 'profile_list.html'


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile_detail.html'


class ProfileCreateView(CreateView):
    model = Profile
    fields = ['user', 'birthday', 'address', 'speciality', 'image']
    template_name = 'profile_form.html'
    success_url = reverse_lazy('profile_list')


class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ['user', 'birthday', 'address', 'speciality', 'image']
    template_name = 'profile_form.html'
    success_url = reverse_lazy('profile_list')


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'profile_confirm_delete.html'
    success_url = reverse_lazy('profile_list')


# Similar CRUD views for the remaining models: Speciality, Diagnoze, TimeTable, and Appointment

# Speciality Views
class SpecialityListView(ListView):
    model = Speciality
    template_name = 'speciality_list.html'


class SpecialityDetailView(DetailView):
    model = Speciality
    template_name = 'speciality_detail.html'


class SpecialityCreateView(CreateView):
    model = Speciality
    fields = ['title', 'is_active']
    template_name = 'speciality_form.html'
    success_url = reverse_lazy('speciality_list')


class SpecialityUpdateView(UpdateView):
    model = Speciality
    fields = ['title', 'is_active']
    template_name = 'speciality_form.html'
    success_url = reverse_lazy('speciality_list')


class SpecialityDeleteView(DeleteView):
    model = Speciality
    template_name = 'speciality_confirm_delete.html'
    success_url = reverse_lazy('speciality_list')


# Diagnoze Views
class DiagnozeListView(ListView):
    model = Diagnoze
    template_name = 'diagnoze_list.html'


class DiagnozeDetailView(DetailView):
    model = Diagnoze
    template_name = 'diagnoze_detail.html'


class DiagnozeCreateView(CreateView):
    model = Diagnoze
    fields = ['title', 'file', 'user']
    template_name = 'diagnoze_form.html'
    success_url = reverse_lazy('diagnoze_list')


class DiagnozeUpdateView(UpdateView):
    model = Diagnoze
    fields = ['title', 'file', 'user']
    template_name = 'diagnoze_form.html'
    success_url = reverse_lazy('diagnoze_list')


class DiagnozeDeleteView(DeleteView):
    model = Diagnoze
    template_name = 'diagnoze_confirm_delete.html'
    success_url = reverse_lazy('diagnoze_list')


# TimeTable Views
class TimeTableListView(ListView):
    model = TimeTable
    template_name = 'timetable_list.html'


class TimeTableDetailView(DetailView):
    model = TimeTable
    template_name = 'timetable_detail.html'


class TimeTableCreateView(CreateView):
    model = TimeTable
    fields = ['doctor', 'date', 'time', 'time_status']
    template_name = 'timetable_form.html'
    success_url = reverse_lazy('timetable_list')


class TimeTableUpdateView(UpdateView):
    model = TimeTable
    fields = ['doctor', 'date', 'time', 'time_status']
    template_name = 'timetable_form.html'
    success_url = reverse_lazy('timetable_list')


class TimeTableDeleteView(DeleteView):
    model = TimeTable
    template_name = 'timetable_confirm_delete.html'
    success_url = reverse_lazy('timetable_list')


# Appointment Views
class AppointmentListView(ListView):
    model = Appointment
    template_name = 'appointment_list.html'


class AppointmentDetailView(DetailView):
    model = Appointment
    template_name = 'appointment_detail.html'


class AppointmentCreateView(CreateView):
    model = Appointment
    fields = ['doctor', 'client', 'timetable']
    template_name = 'appointment_form.html'
    success_url = reverse_lazy('appointment_list')


class AppointmentUpdateView(UpdateView):
    model = Appointment
    fields = ['doctor', 'client', 'timetable']
    template_name = 'appointment_form.html'
    success_url = reverse_lazy('appointment_list')


class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'appointment_confirm_delete.html'
    success_url = reverse_lazy('appointment_list')
