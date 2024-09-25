# serializers.py
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    location_ids = serializers.ListField(
        child=serializers.IntegerField(), write_only=True, required=True
    )  # Expect a list of location IDs from FE

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'email', 'phone_no',
            'location_ids', 'role', 'full_access', 
            'modified_access', 'is_active', 'send_notification'
        ]

    def create(self, validated_data):
        # Extract location IDs from the validated data
        location_ids = validated_data.pop('location_ids')
        user = User.objects.create(**validated_data)

        # Store location_ids directly in the user instance
        user.location_ids = location_ids
        user.save()  # Save the user instance

        return user

    def update(self, instance, validated_data):
        # Extract location IDs if provided
        location_ids = validated_data.pop('location_ids', None)

        # Update user fields
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_no = validated_data.get('phone_no', instance.phone_no)
        instance.role = validated_data.get('role', instance.role)
        instance.full_access = validated_data.get('full_access', instance.full_access)
        instance.modified_access = validated_data.get('modified_access', instance.modified_access)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.send_notification = validated_data.get('send_notification', instance.send_notification)

        if location_ids is not None:
            instance.location_ids = location_ids  # Update location IDs
        instance.save()  # Save the user instance

        return instance

    def to_representation(self, instance):
        """Customize the representation of the serialized user data."""
        representation = super().to_representation(instance)
        representation['location_ids'] = instance.location_ids  # Include location IDs
        return representation
