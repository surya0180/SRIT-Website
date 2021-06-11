from django.contrib import admin
from .models import *

# Register your models here.

class HomeAdmin(admin.ModelAdmin):
    list_display = ('Rollnumber','SemesterTarget','OverallTarget','YourPercentage_predicted','OverallPercentage_predicted')
    
admin.site.register( Home ,HomeAdmin)

class Mid_1Admin(admin.ModelAdmin):
    list_display = ('Rollnumber', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6')

admin.site.register( Mid_1 ,Mid_1Admin)

class Mid_2Admin(admin.ModelAdmin):
    list_display = ('Rollnumber', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6')

admin.site.register( Mid_2 ,Mid_2Admin)

class ExternalAdmin(admin.ModelAdmin):
    list_display = ('Rollnumber', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6')
    
admin.site.register( External ,ExternalAdmin)

class AcademicActivitiesAdmin(admin.ModelAdmin):
    list_display = ('Rollnumber','Subject','DateTime','Link')
    
admin.site.register( AcademicActivities ,AcademicActivitiesAdmin)

class ExtraCurricularActivitiesAdmin(admin.ModelAdmin):
    list_display = ('Rollnumber','Subject','DateTime','Link')
    
admin.site.register( ExtraCurricularActivities ,ExtraCurricularActivitiesAdmin)

class SubjectWiseAdmin(admin.ModelAdmin):
    list_display = ('Rollnumber','Subject','PieChart')
    
admin.site.register( SubjectWise ,SubjectWiseAdmin)

class OverallAdmin(admin.ModelAdmin):
    list_display = ('Rollnumber','BarChart')
    
admin.site.register( Overall ,OverallAdmin)

class ReportAdmin(admin.ModelAdmin):
    list_display = ('Rollnumber', 'point1', 'point2', 'point3', 'point4', 'point5', 'point6', 'point7', 'point8')
    
admin.site.register( Report ,ReportAdmin)

class SuggestionsAdmin(admin.ModelAdmin):
    list_display = ('Rollnumber', 'sug1', 'sug2', 'sug3', 'sug4', 'sug5')
    
admin.site.register( Suggestions ,SuggestionsAdmin)