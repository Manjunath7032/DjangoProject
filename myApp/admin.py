from django.contrib import admin
from myApp.models import student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    l=['number','name','marks']
admin.site.register(student,StudentAdmin)