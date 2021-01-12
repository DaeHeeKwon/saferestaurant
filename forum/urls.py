from django.contrib import admin
from django.urls import path, include, re_path
from forum.views import ForumLV, ForumDV, ForumCreateView, ForumChangeLV, ForumDeleteView, ForumUpdateView

app_name = 'forum'

urlpatterns = [
    path('', ForumLV.as_view(), name="index"),
    re_path(r'^forum/(?P<slug>[-\w]+)/$', ForumDV.as_view(), name="forum_detail"),
    path('add/', ForumCreateView.as_view(), name="add"),
    path('change/', ForumChangeLV.as_view(), name="change"),
    path('<int:pk>/delete/', ForumDeleteView.as_view(), name="delete"),
    path('<int:pk>/update/', ForumUpdateView.as_view(), name="update"),
]