from django.contrib import admin
from .models import AssignedShift, Shift, ShiftAttendance

@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ('name', 'shift_type', 'start_time', 'end_time', 'created_by', 'created_at', 'updated_at','location')
    search_fields = ('id', 'name','shift_type')  # which part of the filed is in the search filed.


@admin.register(AssignedShift)
class AssignedShiftAdmin(admin.ModelAdmin):
    list_display = ('employee', 'shift', 'type', 'assigned_by', 'create_date', 'update_date')
    search_fields = ('employee__username', 'shift__name', 'assigned_by__username', 'id')  # which part of the filed is in the search filed.


@admin.register(ShiftAttendance)
class ShiftAttendanceAdmin(admin.ModelAdmin):
    list_display = ('assigned_shift', 'clocked_in', 'clocked_out', 'total_hours', 'clocked_in_by', 'clocked_out_by')
    search_fields = ('id', 'assigned_shift__employee__username', 'assigned_shift__shift__name')  # which part of the filed is in the search filed.