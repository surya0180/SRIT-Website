from django.db import models

# Create your models here.

class Student(models.Model):
    Username = models.CharField(max_length=25)
    RollNumber = models.CharField(max_length=10)

    def __str__(self):
        return self.Username
    
