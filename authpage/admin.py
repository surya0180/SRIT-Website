from django.contrib import admin
from .models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('Username', 'RollNumber')
    
admin.site.register( Student ,StudentAdmin)
