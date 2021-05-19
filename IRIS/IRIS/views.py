from django.http import HttpResponse
from django.shortcuts import render

from django.utils import timezone

def HomePage(request):
    
    return render(request, 'User/Home.html')