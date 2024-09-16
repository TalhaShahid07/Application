from rest_framework import serializers
from .models import AssignedShift, Shift, ShiftAttendance
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ShiftSerializer(serializers.ModelSerializer):
    
    created_by = UserSerializer(read_only=True)  # Show user details for created_by

    class Meta:
        model = Shift
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class AssignedShiftSerializer(serializers.ModelSerializer):
   
    employee = UserSerializer(read_only=True)  # Show user details for employee
    assigned_by = UserSerializer(read_only=True)  # Show user details for the admin who assigned the shift
    shift = ShiftSerializer(read_only=True)  # Show shift details

    class Meta:
        model = AssignedShift
        fields = '__all__'
        read_only_fields = ['create_date', 'update_date', 'delete_date']


class ShiftAttendanceSerializer(serializers.ModelSerializer):
   
    assigned_shift = AssignedShiftSerializer(read_only=True)  # Show details of the assigned shift
    clocked_in_by = UserSerializer(read_only=True)
    clocked_out_by = UserSerializer(read_only=True)  

    class Meta:
        model = ShiftAttendance
        fields = '__all__'