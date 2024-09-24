from django.db import models
from django.utils import timezone

# Enum choices for the role field
class UserRole(models.TextChoices):
    ADMIN = 'Admin', 'Admin'
    EMPLOYEE = 'Employee', 'Employee'
    MANAGER = 'Manager', 'Manager'

class User(models.Model):
    # User Fields
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Email must be unique
    phone_no = models.CharField(max_length=15)

    # Timestamps for created, updated, deleted (cd, ud, dd)
    created_at = models.DateTimeField(auto_now_add=True)  # cd - created date
    updated_at = models.DateTimeField(auto_now=True)  # ud - updated date
    deleted_at = models.DateTimeField(null=True, blank=True)  # dd - deleted date (nullable)

    # Many-to-Many relationship with Locations (Array of Location IDs)
    locations = models.ManyToManyField('Location')  # Array of location IDs (many-to-many)

    # Enum for user role
    role = models.CharField(
        max_length=10,
        choices=UserRole.choices,
        default=UserRole.EMPLOYEE
    )

    # Notifications and active status
    send_notification = models.BooleanField(default=True)  # Default True
    is_active = models.BooleanField(default=True)  # Default True

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.role})'

class Location(models.Model):
    location_name = models.CharField(max_length=255)

    def __str__(self):
        return self.location_name
