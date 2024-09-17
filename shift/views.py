
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, filters, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils.dateparse import parse_date
from .models import AssignedShift, Shift, ShiftAttendance
from .serializers import AssignedShiftSerializer, ShiftSerializer, ShiftAttendanceSerializer
from .pagination import ShiftPagination #CustomPagination


# Assigned Shift Views

class AssignedShiftListView(generics.GenericAPIView):
    queryset = AssignedShift.objects.all()
    serializer_class = AssignedShiftSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = ShiftPagination
    # pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        shift_id = request.query_params.get('id', None)
        shift_type = request.query_params.get('type', None)
        shift_from = request.query_params.get('shift_from', None)
        shift_to = request.query_params.get('shift_to', None)
        location = request.query_params.get('location', None)

        queryset = self.get_queryset()

        if shift_id:
            try:
                shift = queryset.get(id=shift_id)
                serializer = self.get_serializer(shift)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except AssignedShift.DoesNotExist:
                return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        if shift_type:
            queryset = queryset.filter(type=shift_type)

        if location:
            queryset = queryset.filter(shift__location__icontains=location)
        
        if shift_from and shift_to:
            try:
                shift_from_date = parse_date(shift_from)
                shift_to_date = parse_date(shift_to)
                
                if shift_from_date and shift_to_date:
                    queryset = queryset.filter(
                        shift__start_date__lte=shift_to_date,
                        shift__end_date__gte=shift_from_date
                    )
                else:
                    return Response({"detail": "Invalid date format."}, status=status.HTTP_400_BAD_REQUEST)
            except ValueError:
                return Response({"detail": "Invalid date format."}, status=status.HTTP_400_BAD_REQUEST)

        if not queryset.exists():
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class AssignedShiftDetailView(generics.GenericAPIView):
    queryset = AssignedShift.objects.all()
    serializer_class = AssignedShiftSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            shift = self.get_object()
            serializer = self.get_serializer(shift)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except AssignedShift.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

# Shift Views

class ShiftListCreateView(generics.GenericAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    permission_classes = [IsAuthenticated]
    # pagination_class = CustomPagination
    pagination_class = ShiftPagination
    

    def get(self, request, *args, **kwargs):
        shift_name = request.query_params.get('name', None)

        if shift_name:
            queryset = self.get_queryset().filter(name=shift_name)
            if queryset.exists():
                page = self.paginate_queryset(queryset)
                if page is not None:
                    serializer = self.get_serializer(page, many=True)
                    return self.get_paginated_response(serializer.data)
                serializer = self.get_serializer(queryset, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            queryset = self.get_queryset()
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ShiftDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    permission_classes = [IsAuthenticated]

# Shift Attendance Views

class ShiftAttendanceListCreateView(generics.ListCreateAPIView):
    queryset = ShiftAttendance.objects.all()
    serializer_class = ShiftAttendanceSerializer
    permission_classes = [IsAuthenticated]
    # pagination_class = CustomPagination
    pagination_class = ShiftPagination
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['assigned_shift__employee__username', 'assigned_shift__shift__name', 'id']

    def get_queryset(self):
        queryset = super().get_queryset()
        clocked_in_by = self.request.query_params.get('clocked_in_by', None)
        if clocked_in_by:
            queryset = queryset.filter(clocked_in_by__username=clocked_in_by)
        return queryset

    def perform_create(self, serializer):
        serializer.save(clocked_in_by=self.request.user)

class ShiftAttendanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShiftAttendance.objects.all()
    serializer_class = ShiftAttendanceSerializer
    permission_classes = [IsAuthenticated]

class DeleteShiftView(generics.DestroyAPIView):
    queryset = Shift.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        try:
            return self.destroy(request, *args, **kwargs)
        except Shift.DoesNotExist:
            return Response({"error": "Shift not found."}, status=status.HTTP_404_NOT_FOUND)



