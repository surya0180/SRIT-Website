from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'dashboard.html')

def marks(request):
    return render(request, 'marks.html')

def subjectWise(request):
    return render(request, 'subjectWise.html')

def overall(request):
    return render(request, 'overall.html')

def report(request):
    return render(request, 'report.html')

def suggestion(request):
    return render(request, 'suggestion.html')
