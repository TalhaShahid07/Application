from django.urls import path
from .views import (
    AssignedShiftDetailView,
    ShiftListCreateView, ShiftDetailView,
    ShiftAttendanceListCreateView, ShiftAttendanceDetailView,  DeleteShiftView, AssignedShiftListView)
    # Update this import statement in your urls.py or wherever needed


urlpatterns = [
    path('assigned-shifts/', AssignedShiftListView.as_view(), name='assigned-shift-list'),
    path('assigned-shifts/<int:pk>/', AssignedShiftDetailView.as_view(), name='assigned-shift-detail'),
    path('shifts/', ShiftListCreateView.as_view(), name='shift-list-create'),
    path('shifts/<int:pk>/', ShiftDetailView.as_view(), name='shift-detail'),
    path('shift-attendances/', ShiftAttendanceListCreateView.as_view(), name='shift-attendance-list-create'),
    path('shift-attendances/<int:pk>/', ShiftAttendanceDetailView.as_view(), name='shift-attendance-detail'),
    path('shift/delete/<int:id>/', DeleteShiftView.as_view(), name='delete-shift'),
]
