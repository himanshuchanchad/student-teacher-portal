from django.shortcuts import render

from . import forms,models
from django.contrib.auth.models import User
from django.contrib.auth import logout,login,authenticate


from django.http import  HttpResponseRedirect,HttpResponse
from django.urls import reverse
# Create your views here.

def index(request):
    return render(request,"index.html")

