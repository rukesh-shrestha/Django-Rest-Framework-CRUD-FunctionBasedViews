from django.contrib import admin
from .models import Tasks

# Register your models here.

class CustomTask(admin.ModelAdmin):
    list_display = ['id','title','date','completed']


admin.site.register(Tasks,CustomTask)
