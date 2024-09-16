from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserRegisterSerializer
from rest_framework.response import Response

# Register new user
class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


# class UserRegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# Generate access and refresh token
class TokenObtainPairView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        refresh = RefreshToken.for_user(request.user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })