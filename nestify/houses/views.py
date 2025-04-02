from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import HouseListing
from .serializers import HouseListingSerializer
from rest_framework.response import Response
from .permissions import IsOwnerOrAdmin  # Import the custom permission

class UserHouseListView(generics.ListAPIView):
    serializer_class = HouseListingSerializer
    permission_classes = [IsOwnerOrAdmin]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return HouseListing.objects.filter(listed_by=user_id)


class HouseListingList(generics.ListCreateAPIView):
    queryset = HouseListing.objects.all()
    serializer_class = HouseListingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(listed_by=self.request.user)

class HouseListingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HouseListing.objects.all()
    serializer_class = HouseListingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        if serializer.instance.listed_by != self.request.user:
            raise PermissionDenied("You do not have permission to edit this listing.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.listed_by != self.request.user:
            raise PermissionDenied("You do not have permission to delete this listing.")
        instance.delete()
    

