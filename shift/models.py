from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Shift(models.Model):
    """
    Model representing a work shift with additional location data.
    Each shift has a defined start and end time, type, location, and description.
    """
    SHIFT_TYPE_CHOICES = [
        ('MORNING', 'Morning'),
        ('AFTERNOON', 'Afternoon'),
        ('NIGHT', 'Night'),
    ]
    
    # Fields
    name = models.CharField(max_length=100)  # Name of the shift (e.g., 'Morning Shift', 'Night Shift')
    start_date = models.DateField(null=True)  # Start date of the shift
    end_date = models.DateField(null=True, blank= True)  # End date of the shift
    start_time = models.TimeField(blank = True)  # Start time of the shift
    end_time = models.TimeField(blank = True)  # End time of the shift
    shift_type = models.CharField(max_length=10, choices=SHIFT_TYPE_CHOICES)  # Type of shift: Morning, Afternoon, Night
    location = models.IntegerField(default=1)
    description = models.TextField(blank=True, null=True)  # Optional description of the shift
    created_by = models.ForeignKey(
        User, 
        related_name='created_shifts', 
        on_delete=models.CASCADE
    )  # Admin/manager who created the shift
    created_at = models.DateTimeField(default=timezone.now)  # Timestamp of shift creation
    updated_at = models.DateTimeField(auto_now=True)  # Automatically updated when the shift is modified

    # # Additional Fields
    # max_employees = models.PositiveIntegerField(null=True, blank=True)  # Max number of employees for the shift
    # is_active = models.BooleanField(default=True)  # Indicates whether the shift is active

    # String representation of the shift
    def __str__(self):
        return f"{self.name} ({self.get_shift_type_display()}) - {self.location}"

    class Meta:
        ordering = ['start_date', 'start_time']  # Default ordering of shifts by start date and time
        verbose_name = 'Shift'
        verbose_name_plural = 'Shifts'


class AssignedShift(models.Model):
    """
    Model representing a shift assigned to an employee.
    """
    ASSIGNED = 'ASSIGNED'
    CLOCKED_IN = 'CLOCKED_IN'
    NOT_CLOCKED_IN = 'NOT_CLOCKED_IN'
    
    TYPE_CHOICES = [
        (ASSIGNED, 'Assigned'),
        (CLOCKED_IN, 'Clocked In'),
        (NOT_CLOCKED_IN, 'Not Clocked In'),
    ]
    
    # Fields
    create_date = models.DateTimeField(auto_now_add=True)  # Timestamp when the shift is assigned
    delete_date = models.DateTimeField(null=True, blank=True)  # When shift assignment is deleted, can be null
    update_date = models.DateTimeField(auto_now=True)  # Timestamp when the shift is updated
    employee = models.ForeignKey(
        User, 
        related_name='assigned_shifts', 
        on_delete=models.CASCADE
    )  # Employee assigned the shift, deleted automatically if employee is deleted.
    shift = models.ForeignKey(
        'Shift', 
        related_name='assigned_shifts', 
        on_delete=models.CASCADE
    )  # The shift being assigned, will also be deleted if the shift itself is removed.
    assigned_by = models.ForeignKey(
        User, 
        related_name='assigned_by', 
        on_delete=models.CASCADE
    )  # Admin or manager who assigns the shift.
    type = models.CharField(
        max_length=20, 
        choices=TYPE_CHOICES, 
        default=ASSIGNED
    )  # Current status of the shift assignment: Assigned, Clocked In, or Not Clocked In.

    # String representation of the assigned shift
    def __str__(self):
        return f"{self.employee.username} - {self.shift.name} ({self.get_type_display()})"

    class Meta:
        ordering = ['-create_date']  # Order by the most recent assignments
        verbose_name = 'Assigned Shift'
        verbose_name_plural = 'Assigned Shifts'

#shift Attendence...

class ShiftAttendance(models.Model):

   # for the assigned shifts attendence. ...

    # id = models.AutoField(primary_key=True)
    assigned_shift = models.ForeignKey(AssignedShift, related_name='attendances', on_delete=models.CASCADE)  # FK to AssignedShift
    clocked_in = models.DateTimeField()  # Time the employee clocked in
    clocked_out = models.DateTimeField(null=True, blank=True)  # Time the employee clocked out
    total_hours = models.DurationField(null=True, blank=True)  # Total hours worked
    clocked_in_by = models.ForeignKey(User, related_name='clocked_in_by', on_delete=models.CASCADE, default= User)  # Admin who recorded clock-in
    clocked_out_by = models.ForeignKey(User, related_name='clocked_out_by', on_delete=models.CASCADE, null=True, blank=True)  # Admin who recorded clock-out

    def __str__(self):
        return f"Attendance for {self.assigned_shift.employee.username} ({self.assigned_shift.shift.name})"