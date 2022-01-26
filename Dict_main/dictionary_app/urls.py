
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('',home, name="home-dict"),
    path('word/',word, name='word'),
]
