from django.shortcuts import render
from home import forms
from . import models

from django.contrib.auth.models import User
from django.contrib.auth import logout,login,authenticate


from django.http import  HttpResponseRedirect,HttpResponse
from django.urls import reverse
# Create your views here.
def studentsignup(request):
    if request.method=="POST":
        user=forms.add_user(data=request.POST)
        student=forms.add_student(data=request.POST)

        if user.is_valid and student.is_valid :
            create_user=user.save()
            create_user.set_password(create_user.password)
            create_user.save()
            models.student.create(
                user=user,
                sapid=sapid,
                year =year,
                div =div,
                batch=batch,
                dept=dept
                )
            return HttpResponseRedirect(reverse(student_login))
        else :
            pass
    else :
        user = forms.add_user()
        student = forms.add_student()
    context={
        'user':user,
        'student':student
    }
    return render(request,"student_signup.html",context)

def student_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        if username and password :
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)
                return HttpResponseRedirect(reverse(student_home))
            else:
                return HttpResponse("user doesn't exists or password doesn't match!")
        else:
            return HttpResponse("Enter the password !")
    else:
        return render(request,"student_login.html")