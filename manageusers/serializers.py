# # test works good
# from rest_framework import serializers
# from .models import User, Location

# class LocationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Location
#         fields = ['id', 'location_name']

# class UserSerializer(serializers.ModelSerializer):
#     # Accept only IDs for locations
#     locations = serializers.PrimaryKeyRelatedField(
#         many=True,
#         queryset=Location.objects.all(),
#     )

#     class Meta:
#         model = User
#         fields = [
#             'id', 
#             'first_name', 
#             'last_name', 
#             'email_id', 
#             'phone_number', 
#             'locations', 
#             'send_notification', 
#             'is_active', 
#             'role', 
#             'Full_access', 
#             'Modified_Access'
#         ]

#     def to_representation(self, instance):
#         # Customize the output representation
#         representation = super().to_representation(instance)
#         # Retrieve full location details based on the IDs
#         representation['locations'] = LocationSerializer(instance.locations.all(), many=True).data
#         return representation

#     def create(self, validated_data):
#         locations = validated_data.pop('locations', [])
#         user = User.objects.create(**validated_data)
#         user.locations.set(locations)  # Set locations using IDs
#         return user

#     def update(self, instance, validated_data):
#         locations = validated_data.pop('locations', [])
#         instance.locations.set(locations)  # Update locations
#         return super().update(instance, validated_data)




# final test which is work good...

from rest_framework import serializers
from .models import User, Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['location_name']  # Only keep location_name

class UserSerializer(serializers.ModelSerializer):
    # Accept only IDs for locations
    locations = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Location.objects.all(),
    )

    class Meta:
        model = User
        fields = [
            'id', 
            'first_name', 
            'last_name', 
            'email_id', 
            'phone_number', 
            'locations', 
            'send_notification', 
            'is_active', 
            'role', 
            'Full_access', 
            'Modified_Access'
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Retrieve full location details based on the IDs, but only return names
        representation['locations'] = [location.location_name for location in instance.locations.all()]
        return representation

    def create(self, validated_data):
        locations = validated_data.pop('locations', [])
        user = User.objects.create(**validated_data)
        user.locations.set(locations)  # Set locations using IDs
        return user

    def update(self, instance, validated_data):
        locations = validated_data.pop('locations', [])
        instance.locations.set(locations)  # Update locations
        return super().update(instance, validated_data)