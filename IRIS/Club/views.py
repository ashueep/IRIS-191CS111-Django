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
    itemID = request.POST.get("itemID")
    item = Items.objects.filter(id = itemID).first()
    if request.method == 'POST':
        req = ItemRequest(request.user, item, status = RequestStatus.objects.filter(pk = 1)[0])
        req.save()
        messages.success(request, f'Item requested!')
        return redirect('/')