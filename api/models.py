from django.db import models
from django.contrib.auth.models import AbstractUser


# Custom User Model
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)

    def __str__(self):
        return self.username


# Role Model (defining roles like doctor, client, etc.)
class Role(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


# Profile Model (expanding user data with additional details like birthday, address, etc.)
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)  # One-to-one relationship with CustomUser
    birthday = models.DateField(null=True, blank=True)
    address = models.TextField()
    speciality = models.ForeignKey('Speciality', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/profile_images', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile of {self.user.username}"


# Speciality Model (defining specialties for doctors)
class Speciality(models.Model):
    title = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


# Diagnose Model (stores diagnosis details, including optional file upload)
class Diagnoze(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to='static/diagnoze_files', max_length=100, null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# TimeTable Model (stores available time slots for doctors)
class TimeTable(models.Model):
    doctor = models.ForeignKey(CustomUser, related_name='time_slots', on_delete=models.CASCADE)  # Link to doctors
    date = models.DateField()
    time = models.TimeField()
    time_status = models.BooleanField(default=True)  # True = available, False = not available

    def __str__(self):
        return f"{self.doctor.username} - {self.date} {self.time}"


# Appointment Model (links clients to doctors and timetables)
class Appointment(models.Model):
    doctor = models.ForeignKey(CustomUser, related_name='appointments_as_doctor', on_delete=models.CASCADE)
    client = models.ForeignKey(CustomUser, related_name='appointments_as_client', on_delete=models.CASCADE)
    timetable = models.ForeignKey(TimeTable, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment: {self.client.username} with {self.doctor.username} on {self.timetable.date} at {self.timetable.time}"