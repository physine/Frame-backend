from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from .serializers import *
from .models import *

import json


# ===============================================
#                 Overview
#------------------------------------------------

@api_view(['GET'])
def apiOverview(request):
    json = {
            'password_reset':'/api/password_reset/',
            'login':'/api/login/',
            'create_account':'/api/UserCreate/'
            }
    return Response(json)

# ===============================================
#                 Logged Out
#------------------------------------------------

@api_view(['POST'])
def password_reset(request):
    data = 'a password reset code has been sent to the email address: '+request['email']
    return Response(data)


@api_view(['POST'])
def create_user(request):
    serializer = RegistrationSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        user = serializer.save()
        data['responce'] = 'created account with email: '+user.email+' and username: '+user.username
        data['token'] = Token.objects.get(user=user).key
    else:
        data = serializer.errors
    return Response(data)
    
    
# ===============================================
#                 Logged In - Auth Required
#------------------------------------------------

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def upload_images(request):
    data = 'This is an Authenticated area'
    return Response(data)




