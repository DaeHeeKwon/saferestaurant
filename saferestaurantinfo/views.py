from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'saferestaurantinfo/index.html'

class RestaurantListView(TemplateView):
    template_name = 'saferestaurantinfo/saferestaurantlist.html'