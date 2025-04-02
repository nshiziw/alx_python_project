from django.urls import path
from .views import HouseListingList, HouseListingDetail, UserHouseListView

urlpatterns = [
    path('', HouseListingList.as_view(), name='house-list'),
    path('<int:pk>/', HouseListingDetail.as_view(), name='house-detail'),
    path('user/<int:user_id>/', UserHouseListView.as_view(), name='user-houses'),
]