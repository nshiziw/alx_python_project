from django.urls import path
from .views import HouseListingList, HouseListingDetail, AdminUserListView, AdminUserDetailView, AdminStatisticsView, UserHouseListView

urlpatterns = [
    path('', HouseListingList.as_view(), name='house-list'),
    path('<int:pk>/', HouseListingDetail.as_view(), name='house-detail'),
    path('user/<int:user_id>/', UserHouseListView.as_view(), name='user-houses'),
    
    path('admin/users/', AdminUserListView.as_view(), name='admin-users'),
    path('admin/users/<int:pk>/', AdminUserDetailView.as_view(), name='admin-user-detail'),
    path('admin/statistics/', AdminStatisticsView.as_view(), name='admin-statistics'),
]