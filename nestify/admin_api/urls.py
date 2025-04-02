from django.urls import path
from .views import (
    AdminStatisticsView,
    AdminUserListView,
    AdminUserDetailView,
    AdminUserHousesView
)

urlpatterns = [
    path('statistics/', AdminStatisticsView.as_view(), name='admin-statistics'),
    path('users/', AdminUserListView.as_view(), name='admin-users'),
    path('users/<int:pk>/', AdminUserDetailView.as_view(), name='admin-user-detail'),
    path('users/<int:pk>/houses/', AdminUserHousesView.as_view(), name='admin-user-houses'),
] 