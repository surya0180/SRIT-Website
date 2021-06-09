from django.shortcuts import render, redirect
from .models import Student
from django.contrib.auth.models import User

# Create your views here.

def login(request):
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
        
        user = User.objects.create(username=username, password=password)
        user.is_active = True
        user.save()

        Student.objects.all().create(Username=username, RollNumber=rollnumber)
        
        return redirect('index')

    return render(request, 'signup.html')
