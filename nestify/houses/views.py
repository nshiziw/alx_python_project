from rest_framework import generics, permissions
from .models import HouseListing
from .serializers import HouseListingSerializer
from .serializers import UserSerializer
from users.models import User
from rest_framework.response import Response

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

class AdminUserListView(generics.ListAPIView):
    queryset = User.objects.filter(usertype='property_owner')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

class AdminUserDetailView(generics.RetrieveDestroyAPIView):
    queryset = User.objects.filter(usertype='property_owner')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

class AdminStatisticsView(generics.GenericAPIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        total_houses = HouseListing.objects.count()
        houses_for_rent = HouseListing.objects.filter(status='rent').count()
        houses_for_sale = HouseListing.objects.filter(status='sell').count()
        total_users = User.objects.count()
        return Response({
            'total_houses': total_houses,
            'houses_for_rent': houses_for_rent,
            'houses_for_sale': houses_for_sale,
            'total_users': total_users,
        })