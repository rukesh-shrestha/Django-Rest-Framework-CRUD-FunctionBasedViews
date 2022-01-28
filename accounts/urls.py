from django.contrib import admin
from django.urls import path,include
from .views import RegisterAPIView

urlpatterns = [
    path('accounts/',RegisterAPIView.as_view(),name='register')   
    
]