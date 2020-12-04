from rest_framework import serializers
from .models import *

import datetime


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = Users
        fields = ['email','first_name','last_name','password1','password2']
        extra_kwargs = {
            'pasword1' : {'write_only' : True}
        }
    
    # def save(self):
        
    
class GroupsSerializer(serializers.ModelSerializer):
    class Meta:    
        model = Groups
        fields = ['users_id','group_name']

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:    
        model = Images
        fields = ['users_id','image_name']

class FriendsSerializer(serializers.ModelSerializer):
    class Meta:    
        model = Images
        fields = ['lookup_id','results_id']
