from django.contrib import admin
from django.urls import path, include, re_path
from .views import *


from django.contrib.auth.urls import views
from django.conf.urls import handler404, handler500


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
]