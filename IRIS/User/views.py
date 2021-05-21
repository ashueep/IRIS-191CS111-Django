from django.shortcuts import redirect, render
from .forms import CustUserCreationForm, CustUserChangeForm
from Club.models import ItemRequest, RequestStatus
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import User
# Create your views here.
def UserRegister(request):
    if request.method == 'POST':
        form = CustUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.userName, password=raw_password)
            login(request, user)
            messages.success(request, f'Account for user {user.userName} created successfully!')
            return redirect('/')
    else:
        form = CustUserCreationForm()
    return render(request, 'User/Register.html', {'form' : form})

def YourInventory(request):
    user = request.user
    requestsPending = ItemRequest.objects.filter(memberID = user).filter(status = RequestStatus.objects.all()[1])
    requestsAccepted = ItemRequest.objects.filter(memberID = user).filter(status = RequestStatus.objects.all()[0])
    requestsRejected = ItemRequest.objects.filter(memberID = user).filter(status = RequestStatus.objects.all()[2])

    context = {'pending':requestsPending, 'accepted' : requestsAccepted, 'rejected' : requestsRejected}

    return render(request, 'User/Inventory.html', context)

def YourProfile(request):
    user = request.user
    context = {'user' : user}
    return render(request, 'User/YourProfile.html', context)

def MemberRequest(request, username):
    member = User.objects.filter(userName = username).first()
    requestsPending = ItemRequest.objects.filter(memberID = member).filter(status = RequestStatus.objects.all()[1])
    requestsAccepted = ItemRequest.objects.filter(memberID = member).filter(status = RequestStatus.objects.all()[0])
    requestsRejected = ItemRequest.objects.filter(memberID = member).filter(status = RequestStatus.objects.all()[2])

    context = {'pending':requestsPending, 'accepted' : requestsAccepted, 'rejected' : requestsRejected, 'member' : member}

    return render(request, 'User/Inventory.html', context)