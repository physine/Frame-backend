from django.urls import path, include
from . import views

from rest_framework.decorators import api_view
from rest_framework.response import Response

# TODO: will need to auth before using logged in routes

urlpatterns = [
    # overview
    path('', views.apiOverview, name='api-overview'),
    
    # logged out
    path('password_reset', views.password_reset, name="password_reset"),
    path('login', views.login, name="login"),
    path('UserCreate', views.UserCreate, name="UserCreate"),

    path('UserList', views.UserList, name="UserList"),

    # logged in

]