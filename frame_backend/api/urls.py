from django.urls import path, include
from . import views

from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.authtoken.views import obtain_auth_token

# TODO: will need to auth before using logged in routes

urlpatterns = [
    # overview
    path('', views.apiOverview, name='api-overview'),
    
    # logged out
    path('password_reset', views.password_reset, name="password_reset"),
    path('login', obtain_auth_token, name="login"), # built in Django view
    path('create_user', views.create_user, name="create_user"),

    #('UserList', views.UserList, name="UserList"),

    # logged in
    path('upload_images', views.upload_images, name="upload_images"),


]