from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.hello_world),
    path('user-name', views.userName),
    path('create-user', views.create_user)
]
