from django.urls import path, re_path
from .views import *
from django.shortcuts import redirect

urlpatterns = [
    # path("Registeration/",  UserRegister, name="register"),
    path("Request-Item/", RequestItem, name = "Request Item"),
    path("Manage-Requests/", ManageRequest, name = "Manage Request"),
    path("Accept-Request/", AcceptRequest, name = "Accept Request"),
    path("Reject-Request/", RejectRequest, name = "Reject Request"),
    path("Add-Item/", AddItem, name = "Add Item"),
    path("Club-Detils", ClubMembers, name = 'Club Details'),
]