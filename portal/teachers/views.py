from django.shortcuts import render
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login,authenticate
from  django.contrib import  messages

from home import forms
from django.http import  HttpResponseRedirect,HttpResponse
from django.urls import reverse
from .models import assignment,practical,notes
from home.models import teacher,group
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
            return HttpResponseRedirect(reverse('teacher:login'))
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
                return HttpResponseRedirect(reverse('teacher:teacher_home')) #
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
    teacher_current = teacher.objects.filter(user=request.user).first()
    group_list=group.objects.filter(owner=teacher_current)
    context={
        'group_list':group_list
    }
    return render(request,"teacher_home.html",context)

@login_required
def addassignment(request,pk):
    groups=group.objects.filter(pk=pk).first()
    if request.method=='POST':
        addassignment_form=forms.add_assignment(data=request.POST)
        if addassignment_form.is_valid():
            if 'file' in request.FILES:
                assignment_save = assignment.objects.create(
                    teacher=groups.owner,
                    group=groups,
                    deadline=addassignment_form.cleaned_data['deadline'],
                    title=addassignment_form.cleaned_data['title'],
                    content=addassignment_form.cleaned_data['content'],
                    file=request.FILES['file']
                )
                assignment_save.save()
            else:
                assignment_save=assignment.objects.create(
                    teacher=groups.owner,
                    group=groups,
                    deadline=addassignment_form.cleaned_data['deadline'],
                    title =addassignment_form.cleaned_data['title'],
                    content = addassignment_form.cleaned_data['content'],
                    )
                assignment_save.save()
            return HttpResponseRedirect(reverse('teacher_group_detail',kwargs={'pk':groups.pk}))
    else:
        addassignment_form=forms.add_assignment()
    context={
    'assignment':addassignment_form
    }
    return render(request,"add_assignment.html",context)

@login_required
def addpractical(request,pk):
    groups=group.objects.filter(pk=pk).first()
    if request.method=='POST':
        addpractical_form=forms.add_practical(data=request.POST)
        if addpractical_form.is_valid():
            if 'file' in request.FILES:
                practical_save = assignment.objects.create(
                    teacher=groups.owner,
                    group=groups,
                    deadline=addpractical_form.cleaned_data['deadline'],
                    title=addpractical_form.cleaned_data['title'],
                    content=addpractical_formm.cleaned_data['content'],
                    file=request.FILES['file']
                )
                practical_save.save()
            else:
                assignment_save=assignment.objects.create(
                    teacher=groups.owner,
                    group=groups,
                    deadline=addpractical_form.cleaned_data['deadline'],
                    title =addpractical_form.cleaned_data['title'],
                    content = addpractical_form.cleaned_data['content'],
                    )
                practical_save.save()
            return HttpResponseRedirect(reverse('teacher_group_detail',kwargs={'pk':groups.pk}))
    else:
        addpractical_form=forms.add_practical()
    context={
    'practical':addpractical_form
    }
    return render(request,"add_practical.html",context)


@login_required
def addnotes(request,pk):
    groups=group.objects.filter(pk=pk).first()
    if request.method=='POST':
        addnotes_form=forms.add_notes(data=request.POST)
        if addnotes_form.is_valid():
            if 'file' in request.FILES:
                notes_save = notes.objects.create(
                    teacher=groups.owner,
                    group=groups,
                    deadline=addnotes_form.cleaned_data['deadline'],
                    title=addnotes_form.cleaned_data['title'],
                    content=addnotes_form.cleaned_data['content'],
                    file=request.FILES['file']
                )
                notes_save.save()
            else:
                notes_save=notes.objects.create(
                    teacher=groups.owner,
                    group=groups,
                    deadline=addnotes_form.cleaned_data['deadline'],
                    title =addnotes_form.cleaned_data['title'],
                    content = addnotes_form.cleaned_data['content'],
                    )
                notes_save.save()
            return HttpResponseRedirect(reverse('teacher_group_detail',kwargs={'pk':groups.pk}))
    else:
        addnotes_form=forms.add_notes()
    context={
    'notes':addnotes_form
    }
    return render(request,"add_notes.html",context)