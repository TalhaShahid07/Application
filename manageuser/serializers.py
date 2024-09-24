from rest_framework import serializers
from .models import User, Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'location_name']

class UserSerializer(serializers.ModelSerializer):
    locations = LocationSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'email', 'phone_no', 
            'locations', 'role', 'send_notification', 'is_active', 
            'created_at', 'updated_at', 'deleted_at'
        ]
