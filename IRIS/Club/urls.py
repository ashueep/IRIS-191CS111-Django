from django.urls import path, re_path
from .views import *
from django.shortcuts import redirect

urlpatterns = [
    # path("Registeration/",  UserRegister, name="register"),
    path("Request-Item/", RequestItem, name = "Request Item"),
]