from django.urls import path
from .views import (
    AdminStatisticsView,
    AdminUserListView,
    AdminUserDetailView
)

urlpatterns = [
    path('statistics/', AdminStatisticsView.as_view(), name='admin-statistics'),
    path('users/', AdminUserListView.as_view(), name='admin-users'),
    path('users/<int:pk>/listings/', AdminUserDetailView.as_view(), name='admin-user-listings'),
    path('users/<int:pk>/ban/', AdminUserDetailView.as_view(), name='admin-user-ban'),
    path('users/<int:pk>/delete/', AdminUserDetailView.as_view(), name='admin-user-delete'),
] 