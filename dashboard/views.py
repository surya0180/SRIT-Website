from django.core.files.storage import FileSystemStorage
import numpy as np
from matplotlib import pyplot as plt
from django.shortcuts import render
import random
import matplotlib
matplotlib.use('Agg')
# Create your views here.


def dashboard(request):
    return render(request, 'dashboard.html')


def marks(request):
    return render(request, 'marks.html')


def activities(request):
    return render(request, 'activities.html')


def subjectWise(request):
    labels = 'mid-1', 'mid-2', 'quiz', 'other activities'
    sizes = [random.randint(10, 30), random.randint(
        30, 50), random.randint(30, 50), random.randint(30, 50)]
    explode = (0.05, 0, 0.05, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.axis('equal')
    plt.title("Pie chart of Subject")
    plt.savefig('media/sale_purchase_peichart.png', dpi=100)
    plt.close()

    return render(request, 'subjectWise.html')


def overall(request):
    data = {'subject1': 65, 'subject2': 70,
            'subject3': 85, 'subject4': 56, 'subject5': 74, 'subject6': 60, }

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
