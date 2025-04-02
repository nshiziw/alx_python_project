from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import HouseListing
from .serializers import HouseListingSerializer
from .serializers import UserSerializer
from users.models import User
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

class AdminUserListView(generics.ListAPIView):
    queryset = User.objects.filter(usertype='property_owner')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

class AdminUserDetailView(generics.RetrieveDestroyAPIView):
    queryset = User.objects.filter(usertype='property_owner')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

    def put(self, request, *args, **kwargs):
        user = self.get_object()
        ban_duration = request.data.get('ban_duration')  # Duration in days
        
        if ban_duration is None:
            return Response(
                {'error': 'ban_duration is required'}, 
                status=400
            )
            
        try:
            ban_duration = int(ban_duration)
            if ban_duration <= 0:
                return Response(
                    {'error': 'ban_duration must be positive'}, 
                    status=400
                )
        except ValueError:
            return Response(
                {'error': 'ban_duration must be a valid number'}, 
                status=400
            )
            
        from datetime import datetime, timedelta
        user.is_banned = True
        user.ban_expiry = datetime.now() + timedelta(days=ban_duration)
        user.save()
        
        return Response({
            'message': f'User banned for {ban_duration} days',
            'ban_expiry': user.ban_expiry
        })

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
    

