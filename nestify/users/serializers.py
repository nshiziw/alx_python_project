from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)  # Password is optional for updates

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'usertype', 'password']  

    def validate_password(self, value):
        # Only hash the password if it's provided
        if value:
            return make_password(value)
        return value

    def create(self, validated_data):
        # Handle password during registration
        password = validated_data.pop('password', None)  # Extract password
        user = User.objects.create(**validated_data)  # Create the user with the other fields
        if password:  # If password is provided, hash and save it
            user.set_password(password)
            user.save()
        return user

    def update(self, instance, validated_data):
        # Allow updating the fields that are provided. If password is provided, hash it before saving.
        password = validated_data.get('password', None)
        if password:
            validated_data['password'] = make_password(password)  # Hash the password if it's provided
        return super().update(instance, validated_data)
