from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Role, Profile, Speciality, Diagnoze, TimeTable, Appointment


# CustomUser Admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        *UserAdmin.fieldsets, 
        (
            'Additional Info', {
                'fields': ('phone_number', 'role'),
            },
        ),
    )
    list_display = ['username', 'email', 'phone_number', 'role']


# Role Admin
class RoleAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


# Profile Admin
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'birthday', 'address', 'speciality', 'created_at', 'updated_at']
    search_fields = ['user__username', 'speciality__title']
    list_filter = ['speciality', 'created_at']


# Speciality Admin
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
    search_fields = ['title']
    list_filter = ['is_active']


# Diagnoze Admin
class DiagnozeAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created_at', 'updated_at']
    search_fields = ['title', 'user__username']
    list_filter = ['created_at', 'updated_at']


# TimeTable Admin
class TimeTableAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'date', 'time', 'time_status']
    search_fields = ['doctor__username', 'date']
    list_filter = ['date', 'time_status']


# Appointment Admin
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'client', 'timetable', 'created_at']
    search_fields = ['doctor__username', 'client__username', 'timetable__date']
    list_filter = ['created_at']


# Registering models in admin
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Speciality, SpecialityAdmin)
admin.site.register(Diagnoze, DiagnozeAdmin)
admin.site.register(TimeTable, TimeTableAdmin)
admin.site.register(Appointment, AppointmentAdmin)
