from django.shortcuts import render, redirect
from .models import Student
from django.contrib.auth.models import User
from django.contrib import auth
from dashboard.models import *

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        print(username)
        print(password)
        
        user = auth.authenticate(request, username=username, password=password)
        print(user)
        print(request.user)
        
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {"error": "wrong credentials"})
    
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    # messages.success(request, "Signed out successfully")
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        rollnumber = request.POST['rollnumber']
        password = request.POST['psw']

        if Student.objects.filter(Username = username).exists():
            return redirect('signup')
        if Student.objects.filter(RollNumber = rollnumber).exists():
            return redirect('signup')
        
        user = User.objects.create_user(username=username, password=password)
        user.is_active = True
        user.save()

        Student.objects.all().create(Username=username, RollNumber=rollnumber)
        Home.objects.all().create(Rollnumber=rollnumber)
        Mid_1.objects.all().create(Rollnumber=rollnumber)
        Mid_2.objects.all().create(Rollnumber=rollnumber)
        External.objects.all().create(Rollnumber=rollnumber)

        return redirect('login')

    return render(request, 'signup.html')
