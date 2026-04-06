from django.shortcuts import render, redirect
from .forms import registration_form
from django.contrib.auth.hashers import make_password
from .models import User

# Create your views here.


def login (request):
    return render(request,'account/sign-in.html')


def register(request):
    
    if request.method == 'POST':
        form = registration_form(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            
            user.username = f"{firstname} {lastname}".lower()
            
            rawpassword = form.cleaned_data.get('password')
            user.password = make_password(rawpassword)
            
            print(user)
            
            user.save()
            
            return redirect('login_user')
    else:
        form = registration_form()
    
    return render(request, "account/sign-up.html", {'form':form})

