from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import *

import datetime


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = Users
        fields = ['email','username','password','password2']
        extra_kwargs = {
            'pasword' : {'write_only' : True}
        }
    
    def save(self):
        user = Users(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':'passwords must match'})
        user.set_password(password)
        user.save()
        return user
    
# class GroupsSerializer(serializers.ModelSerializer):
#     class Meta:    
#         model = Groups
#         fields = ['users_id','group_name']

# class ImagesSerializer(serializers.ModelSerializer):
#     class Meta:    
#         model = Images
#         fields = ['users_id','image_name']

# class FriendsSerializer(serializers.ModelSerializer):
#     class Meta:    
#         model = Images
#         fields = ['lookup_id','results_id']
