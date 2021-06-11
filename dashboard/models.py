from django.db import models

# Create your models here.

class Home(models.Model):
    Rollnumber = models.CharField(max_length=10)
    SemesterTarget = models.IntegerField(default=0)
    OverallTarget = models.IntegerField(default=0)
    YourPercentage_predicted = models.IntegerField(default=0)
    OverallPercentage_predicted = models.IntegerField(default=0)

    def __str__(self):
        return self.Rollnumber

class Mid_1(models.Model):
    Rollnumber = models.CharField(max_length=10)
    S1 = models.IntegerField(default=0)
    S2 = models.IntegerField(default=0)
    S3 = models.IntegerField(default=0)
    S4 = models.IntegerField(default=0)
    S5 = models.IntegerField(default=0)
    S6 = models.IntegerField(default=0)

    def __str__(self):
        return self.Rollnumber

class Mid_2(models.Model):
    Rollnumber = models.CharField(max_length=10)
    S1 = models.IntegerField(default=0)
    S2 = models.IntegerField(default=0)
    S3 = models.IntegerField(default=0)
    S4 = models.IntegerField(default=0)
    S5 = models.IntegerField(default=0)
    S6 = models.IntegerField(default=0)

    def __str__(self):
        return self.Rollnumber

class External(models.Model):
    Rollnumber = models.CharField(max_length=10)
    S1 = models.IntegerField(default=0)
    S2 = models.IntegerField(default=0)
    S3 = models.IntegerField(default=0)
    S4 = models.IntegerField(default=0)
    S5 = models.IntegerField(default=0)
    S6 = models.IntegerField(default=0)

    def __str__(self):
        return self.Rollnumber


class AcademicActivities(models.Model):
    Rollnumber = models.CharField(max_length=10)
    Subject = models.CharField(max_length=30)
    DateTime = models.CharField(max_length=40)
    Link = models.CharField(max_length=200)

    def __str__(self):
        return self.Rollnumber

class ExtraCurricularActivities(models.Model):
    Rollnumber = models.CharField(max_length=10)
    Subject = models.CharField(max_length=30)
    DateTime = models.CharField(max_length=40)
    Link = models.CharField(max_length=200)

    def __str__(self):
        return self.Rollnumber

class SubjectWise(models.Model):
    Rollnumber = models.CharField(max_length=10)
    Subject = models.CharField(max_length=30)
    PieChart = models.FileField(upload_to="piecharts/")

    def __str__(self):
        return self.Rollnumber

class Overall(models.Model):
    Rollnumber = models.CharField(max_length=10)
    BarChart = models.FileField(upload_to="barcharts/")

    def __str__(self):
        return self.Rollnumber

class Report(models.Model):
    Rollnumber = models.CharField(max_length=10)
    point1 = models.CharField(max_length=150)
    point2 = models.CharField(max_length=150)
    point3 = models.CharField(max_length=150)
    point4 = models.CharField(max_length=150)
    point5 = models.CharField(max_length=150)
    point6 = models.CharField(max_length=150)
    point7 = models.CharField(max_length=150)
    point8 = models.CharField(max_length=150)

    def __str__(self):
        return self.Rollnumber

class Suggestions(models.Model):
    Rollnumber = models.CharField(max_length=10)
    sug1 = models.CharField(max_length=150)
    sug2 = models.CharField(max_length=150)
    sug3 = models.CharField(max_length=150)
    sug4 = models.CharField(max_length=150)
    sug5 = models.CharField(max_length=150)

    def __str__(self):
        return self.Rollnumber