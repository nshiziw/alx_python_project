from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, permissions
from .serializers import UserSerializer
from .models import User

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Ensures that the current user is returned
        return self.request.user

    def perform_update(self, serializer):
        # Saves the updated user data
        serializer.save()
