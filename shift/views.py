from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from .models import AssignedShift, Shift, ShiftAttendance
from .serializers import AssignedShiftSerializer, ShiftSerializer, ShiftAttendanceSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters, status
from rest_framework.response import Response
# Update this import statement in your urls.py or wherever needed


class AssignedShiftListView(generics.GenericAPIView):
    """
    View to list assigned shifts, filtered by a specific ID or type.
    """
    queryset = AssignedShift.objects.all()
    serializer_class = AssignedShiftSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests for listing assigned shifts, filtered by ID or type.
        """
        shift_id = request.query_params.get('id', None)
        shift_type = request.query_params.get('type', None)

        if shift_id:
            # Filter by exact ID
            try:
                shift = AssignedShift.objects.get(id=shift_id)
                serializer = self.get_serializer(shift)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except AssignedShift.DoesNotExist:
                return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        elif shift_type:
            # Filter by exact type
            queryset = self.get_queryset().filter(type=shift_type)
            if queryset.exists():
                serializer = self.get_serializer(queryset, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            # No filters provided, return all assigned shifts
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
class AssignedShiftDetailView(generics.GenericAPIView):
    """
    View to retrieve a single assigned shift by ID.
    """
    queryset = AssignedShift.objects.all()
    serializer_class = AssignedShiftSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests for retrieving a specific assigned shift.
        """
        try:
            shift = self.get_object()
            serializer = self.get_serializer(shift)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except AssignedShift.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

# Shift Views

class ShiftListCreateView(generics.GenericAPIView):
    """
    View to list all shifts or create a new shift.
    Filtering by name is supported.
    """
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests for listing shifts, filtered by name.
        """
        shift_name = request.query_params.get('name', None)

        if shift_name:
            # Filter by shift name
            queryset = self.get_queryset().filter(name=shift_name)
            if queryset.exists():
                serializer = self.get_serializer(queryset, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            # No filter provided, return all shifts
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        """
        Customizes the creation of a shift.
        Automatically sets the `created_by` field to the current user (admin).
        """
        serializer.save(created_by=self.request.user)

class ShiftDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a shift by ID.
    """
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    permission_classes = [IsAuthenticated]
    
# ShiftAttendance Views
class ShiftAttendanceListCreateView(generics.ListCreateAPIView):
    """
    Lists all shift attendances or creates a new attendance record.
    Authentication is required.
    """
    queryset = ShiftAttendance.objects.all()
    serializer_class = ShiftAttendanceSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['assigned_shift__employee__username', 'assigned_shift__shift__name', 'id']

    def get_queryset(self):
        """
        Optionally filters the returned attendances by clocked_in_by.
        """
        queryset = super().get_queryset()
        clocked_in_by = self.request.query_params.get('clocked_in_by', None)

        if clocked_in_by:
            # queryset = queryset.filter(clocked_in_by=clocked_in_by)
            queryset = queryset.filter(clocked_in_by__username=clocked_in_by)

        
        return queryset

    def perform_create(self, serializer):
        """
        Customizes the creation of a shift attendance.
        Automatically sets the `clocked_in_by` field to the current user (admin).
        """
        serializer.save(clocked_in_by=self.request.user)

class ShiftAttendanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieves, updates, or deletes a shift attendance record.
    Authentication is required.
    """
    queryset = ShiftAttendance.objects.all()
    serializer_class = ShiftAttendanceSerializer
    permission_classes = [IsAuthenticated]

class DeleteShiftView(generics.DestroyAPIView):
    queryset = Shift.objects.all()
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can delete
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        try:
            return self.destroy(request, *args, **kwargs)
        except Shift.DoesNotExist:
            return Response({"error": "Shift not found."}, status=status.HTTP_404_NOT_FOUND)


# have to go to the UK 
#by giving the id with the Url it will delete the user's shift from the data base...
