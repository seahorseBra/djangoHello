from django.urls import re_path
from django.contrib import admin
from django.conf.urls import *
from vote import views

urlpatterns = [
    re_path('a/', views.hello, {'world': 'wepg', 'offset': '9'}),
    re_path('a1/', views.helloSession),
]
