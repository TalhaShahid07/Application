# models.py
from django.db import models

class Location(models.Model):
    location_name = models.CharField(max_length=100)

    def __str__(self):
        return self.location_name


class User(models.Model):
    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('EMPLOYEE', 'Employee'),
        ('MANAGER', 'Manager')
    ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=15)
    role = models.CharField(max_length=10, choices=[('EMPLOYEE', 'Employee'), ('ADMIN', 'Admin'), ('MANAGER', 'Manager')], default='MANAGER')
    full_access = models.BooleanField(default=False)
    modified_access = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    send_notification = models.BooleanField(default=True)
    location_ids = models.JSONField(default=list)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
