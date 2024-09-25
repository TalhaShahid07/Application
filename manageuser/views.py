from rest_framework import generics, filters,status
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()  # Include all users
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    # Update search_fields to remove locations
    search_fields = [
        'first_name',
        'last_name',
        'email',
        'phone_no',
        'role',  # Include role if you want to search by it
        'locations__id', 
#       'locations__location_name'
    ]

    def get_queryset(self):
        queryset = super().get_queryset()  # Get the base queryset

        # Filter by location_ids if provided
        location_ids = self.request.query_params.getlist('location_ids')
        if location_ids:
            queryset = queryset.filter(location_ids__overlap=location_ids)  # Use overlap for filtering
        return queryset

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()  # Include all users
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def perform_destroy(self, instance):
        """Override perform_destroy to perform a soft delete"""
        instance.is_active = False  # Soft delete
        instance.save()

    def delete(self, request, *args, **kwargs):
        """Handle DELETE request to soft delete a user"""
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)