from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import logout,login,authenticate

from home import forms
from . import models
from django.http import  HttpResponseRedirect,HttpResponse
from django.urls import reverse
# Create your views here.
def teachersignup(request):
    if request.method=="POST":
        user=forms.add_user(data=request.POST)
        teacher=forms.add_teacher(data=request.POST)

        if user.is_valid and teacher.is_valid :
            create_user=user.save()
            create_user.set_password(create_user.password)
            create_user.save()
            models.teacher.create(
                user=user,
                dept=dept
                )
            return HttpResponseRedirect(reverse(teacher_login))
        else:
            pass
    else :
        user = forms.add_user()
        teacher = forms.add_teacher()
    context={
        'user':user,
        'teacher':teacher,
    }
    return render(request,"student_signup.html",context)



def teacher_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        if username and password :
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)
                return HttpResponseRedirect(reverse(teacher_home))
            else:
                return HttpResponse("user doesn't exists or password doesn't match!")
        else:
            return HttpResponse("Enter the password !")
    else:
        return render(request,"teacher_login.html")