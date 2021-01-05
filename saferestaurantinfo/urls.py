from django.urls import path


from .views import HomeView, RestaurantListView, SafeRestaurantInfo

app_name = 'saferestaurantinfo'

urlpatterns = [
    path('', HomeView.as_view(), name="index"), # home 연결
    path('saferestaurantlist/', RestaurantListView.as_view(), name="saferestaurantlist"),
    path('saferestaurantlist/<str:region>/', SafeRestaurantInfo.as_view(), name='saferestaurant_region_info'),
]
