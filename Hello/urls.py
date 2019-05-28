"""Hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from vote import views
from django.conf.urls import *
from django.views.generic.list import ListView
from django.contrib.auth.views import auth_login, auth_logout
from vote.admin import VotePeople
from django.views.decorators.cache import cache_page
publish_info = {
    'queryset': VotePeople.objects.all,
    'template_name': 'votepeople.html'
}

urlpatterns = [
    re_path(r'admin/', admin.site.urls),
    re_path('hello/(?P<offset>\d)/(?P<world>.*)', views.hello),
    re_path('hello1', views.hello, {'offset': '3', 'world': 'awoegij我给号'}),
    re_path('hello2/', include('vote.inner')),

    re_path('login', views.login),
    re_path('regiest', views.regiest),

    re_path('votepeople', ListView.as_view, publish_info)
]
