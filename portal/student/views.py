from django.shortcuts import render
from home import forms
from . import models
from django.contrib.auth.models import User

from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.http import  HttpResponseRedirect,HttpResponse
from django.urls import reverse
# Create your views here.
from home.models import students,group

def studentsignup(request):
    if request.method=="POST":
        user=forms.add_user(data=request.POST)
        student=forms.add_student(data=request.POST)

        if user.is_valid() and student.is_valid() :
            create_user=user.save()
            create_user.set_password(create_user.password)
            create_user.save()
            student_create=students.objects.create(
                user=create_user,
                sapid=student.cleaned_data['sapid'],
                year =student.cleaned_data['year'],
                div =student.cleaned_data['div'],
                batch=student.cleaned_data['batch'],
                dept=student.cleaned_data['dept']
                )
            student_create.save()
            return HttpResponseRedirect(reverse('student:login'))
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

@login_required
def student_home(request):
    student_current = students.objects.filter(user=request.user).first()
    group_list = group.objects.filter(member=student_current)
    context = {
        'group_list': group_list
    }

    return render(request, "student_home.html", context)

def student_login(request):
    storage = messages.get_messages(request)
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
                return HttpResponseRedirect(reverse('student:student_home'))
            else:
                messages.warning(request, "Invalid login credentials")
                return render(request, "teacher_login.html", context)
        else:
            messages.warning(request, "Enter username and password ")
            return render(request, "teacher_login.html", context)
    else:
        return render(request,"student_login.html",context)



