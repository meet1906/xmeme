"""xmeme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from buildout.api import *

urlpatterns = [
    path('admin/', admin.site.urls), #admin/ is for admin portal 
    path('memes',  MemesList.as_view(), name='memes_list'), # api/memes - endpoint for getting and posting meme content
    path('memes/<str:meme_id>',MemesListById.as_view(),name='memes_id') # api/memes/<id> - endpoint for getting meme content by unique id.
]



