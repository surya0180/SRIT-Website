from django.shortcuts import render
import random
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import numpy as np
from django.core.files.storage import FileSystemStorage
from .models import Home, Mid_1, Mid_2, External
from authpage.models import Student
# Create your views here.

def dashboard(request):
    if request.method == 'POST':
        sti = request.POST['sti']
        oti = request.POST['oti']
        student = Student.objects.all().filter(Username=request.user.username).get()
        rollnum = student.RollNumber

        Home.objects.all().filter(Rollnumber=rollnum).update(Rollnumber=rollnum, SemesterTarget=sti, OverallTarget=oti)
        details = Home.objects.all().filter(Rollnumber=rollnum).get()
        context = {
            'sti': details.SemesterTarget,
            'oti': details.OverallTarget,
            'stp': details.YourPercentage_predicted,
            'otp': details.OverallPercentage_predicted
        }

        return render(request, 'dashboard.html', context)
    else:
        student = Student.objects.all().filter(Username=request.user.username).get()
        rollnum = student.RollNumber
        details = Home.objects.all().filter(Rollnumber=rollnum).get()
        context = {
            'sti': details.SemesterTarget,
            'oti': details.OverallTarget,
            'stp': details.YourPercentage_predicted,
            'otp': details.OverallPercentage_predicted
        }

        return render(request, 'dashboard.html', context)

def marks(request):
    if request.method == "POST":
        marks = request.POST
        student = Student.objects.all().filter(Username=request.user.username).get()
        rollnum = student.RollNumber

        Mid_1.objects.all().filter(Rollnumber=rollnum).update(
            Rollnumber=rollnum, 
            S1=marks['s1m1'], 
            S2=marks['s2m1'], 
            S3=marks['s3m1'], 
            S4=marks['s4m1'], 
            S5=marks['s5m1'], 
            S6=marks['s6m1']
        )

        Mid_2.objects.all().filter(Rollnumber=rollnum).update(
            Rollnumber=rollnum, 
            S1=marks['s1m2'], 
            S2=marks['s2m2'], 
            S3=marks['s3m2'], 
            S4=marks['s4m2'], 
            S5=marks['s5m2'], 
            S6=marks['s6m2']
        )

        p1 = (int(marks['s1m1'])/30)*100
        p2 = (int(marks['s1m2'])/30)*100
        avg = (p1+p2)/2
        E1 = (avg/100)*40

        p1 = (int(marks['s2m1'])/30)*100
        p2 = (int(marks['s2m2'])/30)*100
        avg = (p1+p2)/2
        E2 = (avg/100)*40

        p1 = (int(marks['s3m1'])/30)*100
        p2 = (int(marks['s3m2'])/30)*100
        avg = (p1+p2)/2
        E3 = (avg/100)*40

        p1 = (int(marks['s4m1'])/30)*100
        p2 = (int(marks['s4m2'])/30)*100
        avg = (p1+p2)/2
        E4 = (avg/100)*40

        p1 = (int(marks['s5m1'])/30)*100
        p2 = (int(marks['s5m2'])/30)*100
        avg = (p1+p2)/2
        E5 = (avg/100)*40

        p1 = (int(marks['s6m1'])/30)*100
        p2 = (int(marks['s6m2'])/30)*100
        avg = (p1+p2)/2
        E6 = (avg/100)*40

        External.objects.all().filter(Rollnumber=rollnum).update(
            Rollnumber=rollnum,
            S1=E1,
            S2=E2,
            S3=E3,
            S4=E4,
            S5=E5,
            S6=E6,
        )

        m1 = Mid_1.objects.filter(Rollnumber=rollnum).get()
        m2 = Mid_2.objects.filter(Rollnumber=rollnum).get()
        e  = External.objects.filter(Rollnumber=rollnum).get()

        context = {
            'm1': m1,
            'm2': m2,
            'e': e,
        }
        return render(request, 'marks.html', context)
    else:
        student = Student.objects.all().filter(Username=request.user.username).get()
        rollnum = student.RollNumber
        m1 = Mid_1.objects.filter(Rollnumber=rollnum).get()
        m2 = Mid_2.objects.filter(Rollnumber=rollnum).get()
        e  = External.objects.filter(Rollnumber=rollnum).get()
        context = {
            'm1': m1,
            'm2': m2,
            'e': e,
        }
        return render(request, 'marks.html', context)

def activities(request):
    return render(request, 'activities.html')

def subjectWise(request):
    labels = 'mid-1', 'mid-2'
    sizes = [random.randint(10,30), random.randint(30,50)]
    explode = (0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig('media/sale_purchase_peichart.png',dpi=100)
    plt.close()
    
    
    return render(request, 'subjectWise.html')

def overall(request):
    return render(request, 'overall.html')

def report(request):
    return render(request, 'report.html')

def suggestion(request):
    return render(request, 'suggestion.html')
