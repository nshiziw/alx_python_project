from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Ensures password is not returned in responses

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'usertype', 'password']  # Added first_name, last_name, password

    def create(self, validated_data):
        password = validated_data.pop('password')  # Extract password before creating the user
        user = User.objects.create(**validated_data)  # Create user with other validated data
        user.set_password(password)  # Hash the password before saving it
        user.save()  # Save the user
        return user
