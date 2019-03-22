from django.shortcuts import render
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login,authenticate
from  django.contrib import  messages

from home import forms
from . import models
from django.http import  HttpResponseRedirect,HttpResponse
from django.urls import reverse

from home.models import teacher
# Create your views here.
def teachersignup(request):
    if request.method=="POST":
        user=forms.add_user(data=request.POST)
        teacher_form=forms.add_teacher(data=request.POST)

        if user.is_valid() and teacher.is_valid() :
            create_user=user.save()
            create_user.set_password(create_user.password)
            create_user.save()
            teachers=teacher.objects.create(
                user=create_user,
                dept=teacher_form.cleaned_data['dept']
                )
            teachers.save()
            return HttpResponseRedirect(reverse(teacher_login))
        else:
            return HttpResponse("error")
    else :
        user = forms.add_user()
        teacher = forms.add_teacher()
    context={
        'user':user,
        'teacher':teacher,
    }
    return render(request,"student_signup.html",context)



def teacher_login(request):
    storage=messages.get_messages(request)
    context = {
        'messages': storage,
    }
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        if username and password :
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)
                return HttpResponseRedirect(reverse(teacher_home))
            else:
                messages.warning(request,"Enter password ")
                return render(request, "teacher_login.html", context)
        else:
            messages.warning(request, "user doesn't exists or password doesn't match!")
            return render(request, "teacher_login.html", context)
    else:
        return render(request,"teacher_login.html",context)

@login_required
def teacher_home(request):

    return render(request,"teacher_home.html",context)