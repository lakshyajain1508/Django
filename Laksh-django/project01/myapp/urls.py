from django.urls import path
from .views import display_profiles

urlpatterns = [
    path('', display_profiles, name='profile_list'),
]