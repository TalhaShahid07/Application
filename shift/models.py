from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Shift(models.Model):
    SHIFT_TYPE_CHOICES = [
        ('MORNING', 'Morning'),
        ('AFTERNOON', 'Afternoon'),
        ('NIGHT', 'Night'),
    ]
    
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    shift_type = models.CharField(max_length=10, choices=SHIFT_TYPE_CHOICES)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='created_shifts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.get_shift_type_display()})"


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
    
    # id = models.AutoField(primary_key=True)
    create_date = models.DateTimeField(auto_now_add=True)  # Timestamp when the shift is assigned
    delete_date = models.DateTimeField(null=True, blank=True)  # When shift assignment is deleted, can be null
    update_date = models.DateTimeField(auto_now=True)  # Timestamp when the shift is updated
    employee = models.ForeignKey(User, related_name='assigned_shifts', on_delete=models.CASCADE)  # Employee assigned the shift, and will get delete automatically if not in the list.
    shift = models.ForeignKey(Shift, related_name='assigned_shifts', on_delete=models.CASCADE)  # The shift being assigned
    assigned_by = models.ForeignKey(User, related_name='assigned_by', on_delete=models.CASCADE)  # Admin who assigns the shift
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default=ASSIGNED)  # Current status of the shift assignment

    def __str__(self):
        return f"{self.employee.username} - {self.shift.name} ({self.get_type_display()})"


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