from django import forms
from .models import student,teacher,assignment,practical,notes,groupmember,group
from django.contrib.auth.models import User
class usercreate(forms.ModelForm):
    password2=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','email','password','password2']

class add_student(forms.ModelForm):
    class Meta:
        model=student
        fields="__all__"
        exclude=['user']

class add_teacher(forms.ModelForm):
    class Meta:
        model=teacher
        fields="__all__"
        exclude=['user']
