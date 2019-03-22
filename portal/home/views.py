from django.shortcuts import render
from django.contrib import messages

from . import forms,models
from django.contrib.auth.models import User
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.decorators import login_required

from django.http import  HttpResponseRedirect,HttpResponse
from django.urls import reverse
# Create your views here.
from teachers.views import teacher_home
from .models import group
def index(request):
    return render(request,"index.html")

@login_required
def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse(index))

def create_group(request):
    storage=messages.get_messages(request)
    if request.method=='POST':
        group_data=forms.create_groups(data=request.POST)
        if group_data.is_valid():
            group_data.save()
            return HttpResponseRedirect(reverse(teacher_home))
        else :
            messages.warning(request,"Invalid data")
            return HttpResponseRedirect(reverse(create_group))
    else:
        group_data=forms.create_groups()
    context={
        'messages':storage,
        'group':group_data
    }
    return render(request,"create_group.html",context)