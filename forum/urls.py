from django.contrib import admin
from django.urls import path, include
from forum.views import ForumLV

urlpatterns = [
    path('', ForumLV.as_view(), name="index"),
    
]