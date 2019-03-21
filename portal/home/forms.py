from django import forms
from .models import groupmember,group
from teachers.models import teacher,assignment,practical,notes
from student.models import student_assignment,student_practical,student
from django.contrib.auth.models import User
class add_user(forms.ModelForm):
    password2=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password','password2']
    def clean(self):
        all_cleaned_data=super().clean()
        password=all_cleaned_data['password']
        password2=all_cleaned_data['password2']
        if password!=password2 :
            raise forms.ValidationError("password doesnt match !")
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

class add_assignment(forms.ModelForm):
    class Meta:
        model=assignment
        fields = "__all__"
        exclude = ['teacher','group']

class add_practical(forms.ModelForm):
    class Meta:
        model=practical
        fields = "__all__"
        exclude = ['teacher','group']

class add_notes(forms.ModelForm):
    class Meta:
        model=notes
        fields = "__all__"
        exclude = ['teacher','group']

class add_student_assignment(forms.ModelForm):
    class Meta:
        model=student_assignment
        fields = "__all__"
        exclude = ['student','assignment']

class add_student_practical(forms.ModelForm):
    class Meta:
        model=student_practical
        fields = "__all__"
        exclude = ['student','practical']
