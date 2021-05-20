from django.shortcuts import redirect, render
from .models import Items, ItemRequest, RequestStatus
from django.contrib import messages
from django.db.models import Q

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
        req = ItemRequest(memberID = request.user, itemID = item, requested = requested, club = item.club, status = RequestStatus.objects.all()[1])
        req.save()
        messages.success(request, f'Item requested!')
        return redirect('/')
    return redirect('/')

def ManageRequest(request):
    user = request.user
    if not user.is_convener:
        messages.error(request, 'You dont have permission to view this page!')
        return redirect('/')
    requests = ItemRequest.objects.filter(club = user.club).filter(status = RequestStatus.objects.all()[1])
    title = f'Manage {user.club} inventory'
    context = {'title' : title, 'requests' : requests}
    return render(request, 'User/ManageRequest.html', context)

def AcceptRequest(request):
    user = request.user
    if not user.is_convener:
        messages.error(request, 'You do not have permission!')
        return redirect('/')
    req = request.POST.get("reqID")
    reqID = ItemRequest.objects.filter(id = req).first()
    print(reqID.itemID.id)
    item = Items.objects.filter(id = reqID.itemID.id).first()
    if request.method == 'POST':
        if item.quantity < reqID.requested:
            messages.error(request, 'Cant accept request due to large request size!')
            return redirect('/club/Manage-Request')
        item.quantity -= reqID.requested
        item.save()
        reqID.status = RequestStatus.objects.all()[0]
        reqID.save()
        messages.success(request, 'Item granted!')
        return redirect('/')

def RejectRequest(request):
    user = request.user
    if not user.is_convener:
        messages.error(request, 'You do not have permission!')
        return redirect('/')
    req = request.POST.get("reqID")
    reqID = ItemRequest.objects.filter(id = req).first()
    print(reqID.itemID.id)
    item = Items.objects.filter(id = reqID.itemID.id).first()
    item = Items.objects.filter(id = reqID.itemID.id).first()
    if request.method == 'POST':
        reqID.status = RequestStatus.objects.all()[2]
        reqID.save()
        messages.success(request, 'Item rejected!')
        return redirect('/')
