from django.shortcuts import render
from home import forms
from . import models
from django.contrib.auth.models import User

from django.db.models import Q
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.http import  HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from teachers.models import assignment,practical
from home.models import students,group
from .models import student_assignment,student_practical

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
    join_group = group.objects.filter(Q(dept=student_current.dept) & Q(year=student_current.year)).exclude(member=student_current)
    group_list = group.objects.filter(member=student_current)
    context = {
        'joingroup': join_group,
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
                return render(request, "student_login.html", context)
        else:
            messages.warning(request, "Enter username and password ")
            return render(request, "student_login.html", context)
    else:
        return render(request,"student_login.html",context)


@login_required
def submitassignment(request,pk,assignpk):
    student = students.objects.filter(user=request.user).first()
    groups=group.objects.filter(pk=pk).first()
    assign=assignment.objects.filter(pk=assignpk).first()
    if request.method=='POST':
        submitassignment_form=forms.add_student_assignment(data=request.POST)
        # if submitassignment_form.is_valid():
        if 'file' in request.FILES:
            assignment_save = student_assignment.objects.create(
                    student=student,
                    group=groups,
                    assignment=assign,
                    file=request.FILES['file'],
                )
            assignment_save.save()
            return HttpResponseRedirect(reverse('student_group_detail', kwargs={'pk': groups.pk}))
    else:
        submitassignment_form=forms.add_student_assignment()
    context={
    'assignment':submitassignment_form
    }
    return render(request,"submit_assignment.html",context)

@login_required
def submitpractical(request,pk,assignpk):
    student=students.objects.filter(user=request.user)
    groups=group.objects.filter(pk=pk).first()
    assign = practical.objects.filter(pk=assignpk).first()
    if request.method=='POST':
        submitpractical_form=forms.add_student_practical(data=request.POST)
        # if submitpractical_form.is_valid():
        if 'file' in request.FILES:
            practical_save = student_practical.objects.create(
                    student=student,
                    group=groups,
                    practical=assign,
                    file=request.FILES['file'],
                )
            practical_save.save()
            return HttpResponseRedirect(reverse('student_group_detail', kwargs={'pk': groups.pk}))
        # else:
        #     print('error')
    else:
        submitpractical_form=forms.add_student_practical()
    context={
    'practical':submitpractical_form
    }
    return render(request,"submit_practical.html",context)

@login_required
def joingroups(request,pk):
    if request.method=="POST":
        groups=group.objects.get(pk=pk)
        student = students.objects.filter(user=request.user).first()
        groups.member.add(student)
        groups.save()
        return HttpResponseRedirect(reverse('student:student_home'))
    else:
        pass
    return render(request,"joingroups.html")