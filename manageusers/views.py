from rest_framework import generics, filters, status
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.filter(is_deleted=False).prefetch_related('locations').order_by('id')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['locations__location_name']  # Allows filtering user list by location name

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(is_deleted=False).prefetch_related('locations')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.soft_delete()  # Perform a soft delete by setting is_deleted to True
        print("The data of that instance is deleted")  # This will print to the console
        return Response(status=status.HTTP_204_NO_CONTENT)