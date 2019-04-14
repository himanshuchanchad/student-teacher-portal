from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate
from  django.contrib import  messages

from home import forms
from django.http import  HttpResponseRedirect,HttpResponse
from django.urls import reverse
from .models import assignment,practical,notes
from home.models import teacher,group
from student.models import student_assignment,student_practical
# Create your views here.
from teachers.docxtopdf import converter

def teachersignup(request):
    if request.method=="POST":
        user=forms.add_user(data=request.POST)
        teacher_form=forms.add_teacher(data=request.POST)

        if user.is_valid() and teacher_form.is_valid() :
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
        teacher_form = forms.add_teacher()
    context={
        'user':user,
        'teacher_form':teacher_form,
    }
    return render(request,"teacher_signup.html",context)



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
    if (teacher.objects.filter(user=request.user).exists()):
        teacher_current = teacher.objects.filter(user=request.user).first()
        group_list = group.objects.filter(owner=teacher_current)
        context = {
            'group_list': group_list
        }
        return render(request, "teacher_home.html", context)
    else:
        return HttpResponseRedirect(reverse("index"))



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
                practical_save = practical.objects.create(
                    teacher=groups.owner,
                    group=groups,
                    deadline=addpractical_form.cleaned_data['deadline'],
                    title=addpractical_form.cleaned_data['title'],
                    content=addpractical_form.cleaned_data['content'],
                    file=request.FILES['file']
                )
                practical_save.save()
            else:
                practical_save=practical.objects.create(
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

@login_required
def viewassignment(request,assignpk):
    try :
        assignment_list=student_assignment.objects.filter(assignment=assignpk)
    except :
        assignment_list=None
    context={
        'assignment_list':assignment_list
    }
    return render(request,"view_assignment.html",context)

@login_required
def viewpractical(request,assignpk):
    try :
        practical_list=student_practical.objects.filter(practical=assignpk)
    except :
        practical_list=None
    context={
        'practical_list':practical_list
    }
    return render(request,"view_practical.html",context)

@login_required
def viewnotes(request,assignpk):
    try :
        notes_list=notes.objects.filter(pk=assignpk)
    except :
        notes_list=None
    context={
        'notes_list':notes_list
    }
    return render(request,"view_notes.html",context)


@login_required
def teacher_view_all(request,type,pk):
    if type=='assignment':
        assignment_view=student_assignment.objects.get(pk=pk)
        # if(assignment_view.file.path.endswith('.docx')):
        #     print('inside')
        #     path=converter(assignment_view.file.path,"assignment",name="newfile.pdf")
        # else:
        #     path=None
        context={
        # 'path':path,
        'type':'Assignment',
        'view':assignment_view
             }
        return render(request,"teacher_view_all.html",context)
    elif type=='practical':
        practical_view=practical.objects.get(pk=pk)
        context = {
            'type': 'Practical',
            'view': practical_view
        }
        return render(request, "teacher_view_all.html", context)
    else:
        notes_view=notes.objects.get(pk=pk)
        context = {
            'type': 'Notes',
            'view': notes_view
        }
        return render(request, "teacher_view_all.html", context)
