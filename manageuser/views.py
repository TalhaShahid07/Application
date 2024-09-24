from rest_framework import generics, viewsets, filters, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone
from .models import User
from .serializers import UserSerializer

# ListCreateAPIView allows both listing and creating records
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.filter(is_active=True)  # Only show active users
    serializer_class = UserSerializer

# DetailView for retrieving individual user details
class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer

# UpdateView for editing user details
class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name', 'email', 'phone_no']

    # Override the destroy method to implement soft delete
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False  # Set 'is_active' to False for soft delete
        instance.deleted_at = timezone.now()  # Set the deleted timestamp
        instance.save()
        return Response({"message": "User soft deleted."}, status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'])
    def inactive(self, request):
        """Retrieve all inactive (soft-deleted) users."""
        queryset = User.objects.filter(is_active=False)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
