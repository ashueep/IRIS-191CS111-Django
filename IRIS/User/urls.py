from django.urls import path, re_path
from .views import *
from django.shortcuts import redirect

urlpatterns = [
    path("Registeration/",  UserRegister, name="register"),
    path("Your-Inventory/", YourInventory, name = 'Your Inventory'),
    path("Your-Profile/", YourProfile, name = 'Your Profile'),
]