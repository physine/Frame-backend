from rest_framework import serializers
from .models import *

import datetime


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['password_hash','email','first_name','last_name']
    
    # def __init__(self, date=datetime.datetime.now()):
    #     pass

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
