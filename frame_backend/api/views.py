from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response


# ===============================================
#                 Overview
#------------------------------------------------

@api_view(['GET'])
def apiOverview(request):
    json = {'password_reset':'/api/password_reset/', 'login':'/api/login/'}
    return Response(json)

# ===============================================
#                 Logged Out
#------------------------------------------------

@api_view(['POST'])
def password_reset(request):
    json = {'password_reset':'ENDPOINT WORKING'}
    return Response(json)

@api_view(['POST'])
def login(request):
    json = {'login':'ENDPOINT WORKING'}
    return Response(json)

# ===============================================
#                 Logged In - Auth Required
#------------------------------------------------



