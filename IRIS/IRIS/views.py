from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.utils import timezone

from Club.models import Items

def HomePage(request):
    user = request.user
    print(user.is_authenticated)
    if not user.is_authenticated:
        return redirect('/login')
    userInventory = Items.objects.filter(club = request.user.club).filter(quantity__gt = 0)
    print(userInventory)
    context = {'title' : 'Your Inventory', 'inv' : userInventory}
    return render(request, 'User/Home.html', context)