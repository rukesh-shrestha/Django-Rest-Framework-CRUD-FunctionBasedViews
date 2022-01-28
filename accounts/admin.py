from django.contrib import admin
from .models import  User

# Register your models here.

class CustomUser(admin.ModelAdmin):
    list_display = ['username','email','is_staff','is_superuser']
    
    
admin.site.register(User,CustomUser)
