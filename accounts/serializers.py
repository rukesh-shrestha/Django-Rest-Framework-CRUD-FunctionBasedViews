from .models import User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers



class RegisterSerializer(ModelSerializer):
    password = serializers.CharField(max_length=128,min_length=6,write_only=True)
    class Meta:
        model = User
        fields = ('username','email','password',)
        
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
        
        