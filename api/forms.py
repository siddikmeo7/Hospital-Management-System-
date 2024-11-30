from django import forms
from .models import *


# CustomUser Form
class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'role']


# Role Form
class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['title']


# Profile Form
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'birthday', 'address', 'speciality', 'image']


# Speciality Form
class SpecialityForm(forms.ModelForm):
    class Meta:
        model = Speciality
        fields = ['title', 'is_active']


# Diagnoze Form
class DiagnozeForm(forms.ModelForm):
    class Meta:
        model = Diagnoze
        fields = ['title', 'file', 'user']


# TimeTable Form
class TimeTableForm(forms.ModelForm):
    class Meta:
        model = TimeTable
        fields = ['doctor', 'date', 'time', 'time_status']


# Appointment Form
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'client', 'timetable']
