from django.shortcuts import render
from django.contrib import messages

from . import forms
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.http import  HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from teachers.models import assignment,practical,notes
from .models import group,teacher,students
from student.models import student_assignment,student_practical

def index(request):
    return render(request,"index.html")

@login_required
def logoutrequest(request):
    logout(request)
    return HttpResponseRedirect(reverse(index))

@login_required
def create_group(request):
    storage=messages.get_messages(request)
    if request.method=='POST':
        group_data=forms.create_groups(data=request.POST)
        teacher_current=teacher.objects.filter(user=request.user).first()
        if group_data.is_valid():
            gr=group.objects.create(
            owner=teacher_current,
            name =group_data.cleaned_data['name'],
            sub = group_data.cleaned_data['sub'],
            division = group_data.cleaned_data['division'],
            div = group_data.cleaned_data['div'],
            batch =group_data.cleaned_data['batch'],
            batch_check=group_data.cleaned_data['batch_check'],
            year = group_data.cleaned_data['year'],
            dept = group_data.cleaned_data['dept'],
            )
            gr.save()
            return HttpResponseRedirect(reverse('teacher:teacher_home'))
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

@login_required
def teacher_group_detail(request,pk):
    group_detail=group.objects.get(pk=pk)
    try :
        assignments=assignment.objects.filter(group=group_detail)
        print(assignment)
    except:
        assignments = None
    try :
        note=notes.objects.filter(group=group_detail)
    except:
        note = None
    try :
        practicals=practical.objects.filter(group=group_detail)
    except:
        practicals=None
    context={
        'group':group_detail,
        'assignment':assignments,
        'practical':practicals,
        'notes':note,
    }
    return render(request,"teacher_group_detail.html",context)

@login_required
def student_group_detail(request,pk):
    group_detail=group.objects.get(pk=pk)
    student=students.objects.get(user=request.user)
    try :
        submitted_assignment=student_assignment.objects.filter(student=student)
        temp1=[]
        for s in submitted_assignment:
            temp1.append(s.assignment)
        assignments=assignment.objects.filter(group=group_detail).exclude(title__in=temp1)

    except:
        print("wrroeasdsacas")
        assignments = None
    try :
        note=notes.objects.filter(group=group_detail)
    except:
        note = None
    try :
        submitted_practical=student_practical.objects.filter(student=student)
        temp2=[]
        for s in submitted_practical:
            temp2.append(s.practical)
        practicals=practical.objects.filter(group=group_detail).exclude(title__in=temp2)
    except:
        practicals=None
    context={
        'group':group_detail,
        'assignment':assignments,
        'practical':practicals,
        'notes':note,
    }
    return render(request,"student_group_detail.html",context)

