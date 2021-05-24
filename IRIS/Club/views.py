from django.shortcuts import redirect, render
from .models import Items, ItemRequest, RequestStatus
from django.contrib import messages
from django.db.models import Q
from User.models import User
from .forms import ItemForm
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
    if request.user.club != item.club:
        messages.error(request, 'Error in requesting Item!')
        return redirect('/')
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

def AddItem(request):
    club = request.user.club
    if not request.user.is_convener:
        messages.error(request, 'You do not have the permission!')
        return redirect('/')
    
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.club = club
            instance.save()
            messages.success(request, 'Item added successfully!')
            return redirect('/')
    else:
        form = ItemForm()
    return render(request, 'Club/CreateItem.html', {'form' : form})

def ClubMembers(request):
    user = request.user
    if not user.is_convener:
        messages.error(request, 'You do not have permission to view this page')
        return redirect('/')
    members = User.objects.filter(club = user.club)
    context = {'title' : f'{user.club} Details', 'members' : members}
    return render(request, 'Club/ClubDetails.html', context)

def DeleteInventory(request):
    user = request.user
    # print('HI')
    if not user.is_convener:
        messages.error(request, 'You do not have permissions to view this page!')
        return redirect('/')
    
    items = Items.objects.filter(club = user.club)

    context = {'items' : items}

    if request.method == 'POST':
        # print('in post')
        items = request.POST.getlist('checks[]')
        print(items)
        for item in items:
            todel = Items.objects.filter(id = item)
            if todel.club == user.club:
                Items.objects.filter(id = item).delete()
        # print(items)
        return redirect('/club/Delete-Inventory/')

    return render(request, 'Club/DeleteItem.html', context)