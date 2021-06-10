from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('marks/', views.marks, name="marks"),
    path('subjectWise/', views.subjectWise, name="subjectWise"),
    path('overall/', views.overall, name="overall"),
    path('report/', views.report, name="report"),
    path('suggestion/', views.suggestion, name="suggestion"),
]
