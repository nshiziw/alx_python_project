from rest_framework import serializers
from .models import HouseListing

class HouseListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseListing
        fields = '__all__'



from django.contrib.auth.models import User  # Adjust this if using a custom user model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # Add other necessary fields
