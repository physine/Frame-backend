from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import json


# ===============================================
#                 Overview
#------------------------------------------------

@api_view(['GET'])
def apiOverview(request):
    json = {
            'password_reset':'/api/password_reset/',
            'login':'/api/login/',
            'create_account':'/api/create_account/'
            }
    return Response(json)

# ===============================================
#                 Logged Out
#------------------------------------------------

@api_view(['POST'])
def password_reset(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    email = body['email']

    # TODO: create a temp reset password code and email it to the user
    # TODO: if the code is used sucessfully remove it from the db, if the expires also remove it
    # TODO: from the db.  

    return Response(email)

@api_view(['POST'])
def login(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    email = body['email']
    password = body['password']

    # TODO: check if these exists a user with the given email, if so, check if the 
    # TODO: password matches, if it does return a new auth token to the client.
    # TODO: if any of these fail return 'failed to login' to the client.

    return Response(json)

@api_view(['POST'])
def create_account(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    email = body['email']
    first_name = body['fname']
    last_name = body['lname']
    password = body['password']

    # TODO: sanatise user input
    # TODO: check if the email is already in the db, if it is retuen 'account accociated with this email'
    # TODO: if not create a new account the the given details.

    #print(content)
    return Response(body['password'])

# ===============================================
#                 Logged In - Auth Required
#------------------------------------------------





