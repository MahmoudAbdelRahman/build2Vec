from django.shortcuts import render, redirect , HttpResponse
from django.views.generic import View
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from  django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.http import JsonResponse

from django.conf import settings
import copy

from django.core.files.storage import default_storage
from django.core.files import File


import random
import json



from .models import *


from google.cloud import storage
import uuid




class IndexView(View):
    def get(self, request):
        
        return render(request, "basic/index.html")
    
