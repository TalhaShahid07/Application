from django.db import models

from django.contrib.postgres.fields import ArrayField

class Location(models.Model):
    location_name = models.CharField(max_length=255)

    def __str__(self):
        return self.location_name 

class User(models.Model):
    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('MANAGE', 'Manager'),
        ('EMPLOYEE', 'Employee')
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_id = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    locations = models.ManyToManyField(Location, related_name='users')  # Using ManyToManyField for multiple locations per user
    send_notification = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    Full_access = models.BooleanField(default=False)
    Modified_Access = models.BooleanField(default=False)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='EMPLOYEE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def soft_delete(self):
        self.is_deleted = True
        self.save()