from django.urls import path


from .views import HomeView, RestaurantListView, SafeRestaurantInfo, SafeRestaurantDetailView, HomeInfoView

app_name = 'saferestaurantinfo'

urlpatterns = [
    path('', HomeView.as_view(), name="index"), # home 연결
    path('index/', HomeInfoView.as_view(), name="infoindex"),
    path('saferestaurantlist/', RestaurantListView.as_view(), name="saferestaurantlist"),
    path('saferestaurantlist/<str:region>/', SafeRestaurantInfo.as_view(), name='saferestaurant_region_info'),
    path('<str:pk>/', SafeRestaurantDetailView.as_view(), name="saferestaurant_detail"),

]
