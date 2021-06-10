from django.shortcuts import render
import random
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import numpy as np
from django.core.files.storage import FileSystemStorage
# Create your views here.

def dashboard(request):
    return render(request, 'dashboard.html')

def marks(request):
    return render(request, 'marks.html')

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
