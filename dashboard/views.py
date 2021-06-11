from authpage.models import Student
from .models import Home, Mid_1, Mid_2, External
from django.core.files.storage import FileSystemStorage
import numpy as np
from matplotlib import pyplot as plt
from django.shortcuts import render
import random
import matplotlib
matplotlib.use('Agg')
# Create your views here.


def dashboard(request):
    if request.method == 'POST':
        sti = request.POST['sti']
        oti = request.POST['oti']
        student = Student.objects.all().filter(Username=request.user.username).get()
        rollnum = student.RollNumber

        Home.objects.all().filter(Rollnumber=rollnum).update(
            Rollnumber=rollnum, SemesterTarget=sti, OverallTarget=oti)
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
        e = External.objects.filter(Rollnumber=rollnum).get()

        context = {
            'm1': m1,
            'm2': m2,
            'e': e,
        }
        mid1avg = (int(marks['s1m1']) + int(marks['s2m1']) + int(marks['s3m1']) + int(marks['s4m1']) + int(marks['s5m1']) + int(marks['s6m1']))/6
        mid2avg = (int(marks['s1m2']) + int(marks['s2m2']) + int(marks['s3m2']) + int(marks['s4m2']) + int(marks['s5m2']) + int(marks['s6m2']))/6
        extavg = (E1 + E2 + E3 + E4 + E5 + E6)/6
        total = mid1avg+mid2avg+extavg

        Home.objects.all().filter(Rollnumber=rollnum).update(YourPercentage_predicted=total, OverallPercentage_predicted=total)
        return render(request, 'marks.html', context)
    else:
        student = Student.objects.all().filter(Username=request.user.username).get()
        rollnum = student.RollNumber
        m1 = Mid_1.objects.filter(Rollnumber=rollnum).get()
        m2 = Mid_2.objects.filter(Rollnumber=rollnum).get()
        e = External.objects.filter(Rollnumber=rollnum).get()
        context = {
            'm1': m1,
            'm2': m2,
            'e': e,
        }
        return render(request, 'marks.html', context)


def activities(request):
    return render(request, 'activities.html')


def subjectWise(request):

    student = Student.objects.all().filter(Username=request.user.username).get()
    rollnum = student.RollNumber
    m1 = Mid_1.objects.filter(Rollnumber=rollnum).get()
    m2 = Mid_2.objects.filter(Rollnumber=rollnum).get()

    # pie chart 1
    labels = 'mid-1', 'mid-2', 'quiz', 'other activities'
    sizes = [m1.S1, m2.S1, random.randint(10, 20), random.randint(10, 20)]
    # only "explode" the 2nd slice (i.e. 'Hogs')
    explode = (0.1, 0.1, 0.1, 0.1)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.axis('equal')
    plt.title("Pie chart of Subject 1")
    plt.savefig('media/subjectwise_peichart1.png', dpi=100)
    plt.close()
    # pie chart 2
    labels = 'mid-1', 'mid-2', 'quiz', 'other activities'
    sizes = [m1.S2, m2.S2, random.randint(10, 20), random.randint(10, 20)]

    fig2, ax2 = plt.subplots()
    ax2.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax2.axis('equal')
    plt.title("Pie chart of Subject 2")
    plt.savefig('media/subjectwise_peichart2.png', dpi=100)
    plt.close()
    # pie chart 3
    labels = 'mid-1', 'mid-2', 'quiz', 'other activities'
    sizes = [m1.S3, m2.S3, random.randint(10, 20), random.randint(10, 20)]

    fig3, ax3 = plt.subplots()
    ax3.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax3.axis('equal')
    plt.title("Pie chart of Subject 3")
    plt.savefig('media/subjectwise_peichart3.png', dpi=100)
    plt.close()
    # pie chart 4
    labels = 'mid-1', 'mid-2', 'quiz', 'other activities'
    sizes = [m1.S4, m2.S4, random.randint(10, 20), random.randint(10, 20)]

    fig4, ax4 = plt.subplots()
    ax4.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax4.axis('equal')
    plt.title("Pie chart of Subject 4")
    plt.savefig('media/subjectwise_peichart4.png', dpi=100)
    plt.close()
    # pie chart 5
    labels = 'mid-1', 'mid-2', 'quiz', 'other activities'
    sizes = [m1.S5, m2.S5, random.randint(10, 20), random.randint(10, 20)]

    fig5, ax5 = plt.subplots()
    ax5.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax5.axis('equal')
    plt.title("Pie chart of Subject 5")
    plt.savefig('media/subjectwise_peichart5.png', dpi=100)
    plt.close()
    # pie chart 6
    labels = 'mid-1', 'mid-2', 'quiz', 'other activities'
    sizes = [m1.S6, m2.S6, random.randint(10, 20), random.randint(10, 20)]

    fig6, ax6 = plt.subplots()
    ax6.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax6.axis('equal')
    plt.title("Pie chart of Subject 6")
    plt.savefig('media/subjectwise_peichart6.png', dpi=100)
    plt.close()

    return render(request, 'subjectWise.html')


def overall(request):
    student = Student.objects.all().filter(Username=request.user.username).get()
    rollnum = student.RollNumber
    m1 = Mid_1.objects.filter(Rollnumber=rollnum).get()
    m2 = Mid_2.objects.filter(Rollnumber=rollnum).get()
    subject1 = (m1.S1 + m2.S1)*100/60
    subject2 = (m1.S2 + m2.S2)*100/60
    subject3 = (m1.S3 + m2.S3)*100/60
    subject5 = (m1.S5 + m2.S5)*100/60
    subject4 = (m1.S4 + m2.S4)*100/60
    subject6 = (m1.S6 + m2.S6)*100/60

    data = {'subject1': subject1, 'subject2': subject2,
            'subject3': subject3, 'subject4': subject4, 'subject5': subject5, 'subject6': subject6, }

    courses = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))
    my_colors = ['red', 'blue', 'green', 'cyan', 'Purple', 'pink']
    # creating the bar plot
    plt.bar(courses, values, color=my_colors,
            width=0.4)

    plt.xlabel("Subjects")
    plt.ylabel("Score in Each Subject")
    plt.title("Overall Trends")
    plt.savefig('media/overall_barchart.png', dpi=100)
    plt.close()
    return render(request, 'overall.html')


def report(request):
    return render(request, 'report.html')


def suggestion(request):
    return render(request, 'suggestion.html')
