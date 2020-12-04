from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
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
    # TODO: create a temp reset password code and email it to the user
    # TODO: if the code is used sucessfully remove it from the db, if the expires also remove it
    # TODO: from the db.  
    return Response()

@api_view(['POST'])
def login(request):
    # TODO: check if these exists a user with the given email, if so, check if the 
    # TODO: password matches, if it does return a new auth token to the client.
    # TODO: if any of these fail return 'failed to login' to the client.
    return Response()

@api_view(['POST'])
def user_create(request):
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("ok-saved-user")
    #return Response(serializer.errors)
    return Response("errors")


@api_view(['GET'])
def UserList(request):
    users = Users.objects.all()
    serializer = RegistrationSerializer(users, many=True)
    return Response(serializer.data) 
    
    
    # TODO: sanatise user input
    # TODO: check if the email is already in the db, if it is retuen 'account accociated with this email'
    # TODO: if not create a new account the the given details.

# ===============================================
#                 Logged In - Auth Required
#------------------------------------------------





