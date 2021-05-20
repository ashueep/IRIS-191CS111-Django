from django.shortcuts import redirect, render
from .models import Items, ItemRequest, RequestStatus
from django.contrib import messages
# Create your views here.
def YourInventory(request):
    user = request.user
    userInventory = Items.objects.filter(club = request.user.club).filter(quantity__gt = 0)
    print(userInventory)
    context = {'title' : 'Your Inventory', 'inv' : userInventory}
    return render(request, 'User/Home.html', context)


def RequestItem(request):
    print('request item')
    itemID = request.POST.get("itemID")
    requested = request.POST.get("requested")
    print(itemID + " " + requested)
    item = Items.objects.filter(id = itemID).first()
    print(item)
    if request.method == 'POST':
        req = ItemRequest(memberID = request.user, itemID = item, requested = requested ,status = RequestStatus.objects.all()[1])
        req.save()
        messages.success(request, f'Item requested!')
        return redirect('/')
    return redirect('/')