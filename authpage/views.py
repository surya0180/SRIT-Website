from django.shortcuts import render, redirect
from .models import Student
from django.contrib.auth.models import User
from django.contrib import auth

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
            return redirect('index')
        else:
            return render(request, 'login.html', {"error": "wrong credentials"})
    
    return render(request, 'login.html')

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
        
        return redirect('index')

    return render(request, 'signup.html')
