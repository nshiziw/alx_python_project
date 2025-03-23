from rest_framework import serializers
from .models import HouseListing

class HouseListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseListing
        fields = '__all__'