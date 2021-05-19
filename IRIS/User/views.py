from django.shortcuts import redirect, render
from .forms import CustUserCreationForm, CustUserChangeForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
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