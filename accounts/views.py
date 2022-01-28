from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import RegisterSerializer,LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import  authenticate
# Create your views here.

class RegisterAPIView(GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message":"Created successfully!!!"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer
    def post(self,request):
        email = request.data.get('email',None)
        password = request.data.get('password',None)
        
        user = authenticate(username=email, password=password)
        
        if user:
            serializer = self.serializer_class(user)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({"Message":"Invalid credentials!!!"},status=status.HTTP_401_UNAUTHORIZED)