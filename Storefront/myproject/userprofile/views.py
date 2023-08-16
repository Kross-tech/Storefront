from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Userprofile

def vendor_admin(request):
    return render(request, 'vendor_admin.html')

@login_required
def myaccount(request):
    return render(request, 'myaccount.html')
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            userprofile = Userprofile.objects.create(user=user)

            return redirect('index')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {
        'form': form
    })
