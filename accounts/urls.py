from django.contrib import admin
from django.urls import path,include
from .views import RegisterAPIView,LoginAPIView

urlpatterns = [
    path('accounts/',RegisterAPIView.as_view(),name='register'),   
    path('accounts/login/',LoginAPIView.as_view(),name='login')   
    
]