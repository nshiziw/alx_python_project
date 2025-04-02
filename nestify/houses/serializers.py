from rest_framework import serializers
from .models import HouseListing

class HouseListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseListing
        fields = '__all__'
        read_only_fields = ('listed_by', 'date_created')

    def validate_images(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Images must be a list")
        if len(value) < 3:
            raise serializers.ValidationError("At least 3 images are required")
        if len(value) > 5:
            raise serializers.ValidationError("Maximum 5 images allowed")
        return value

    def validate_nearby_amenities(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Nearby amenities must be a list")
        return value

from django.contrib.auth.models import User  # Adjust this if using a custom user model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # Add other necessary fields
