from django.db import models
from django.contrib.auth.models import User
from home.models import group,teacher
# Create your models here.


class assignment(models.Model):
    teacher=models.ForeignKey(teacher,on_delete=models.CASCADE)
    group=models.ForeignKey(group,on_delete=models.CASCADE)
    created = models.DateField(auto_now=True)
    title=models.CharField(max_length=50,blank=False)
    content=models.TextField(blank=True)
    file = models.FileField(upload_to="assignment",blank=True,null=True)
    deadline = models.DateField()

    def __str__(self):
        return self.title

class practical(models.Model):
    teacher=models.ForeignKey(teacher,on_delete=models.CASCADE)
    group=models.ForeignKey(group,on_delete=models.CASCADE)
    created=models.DateField(auto_now=True)
    title = models.CharField(max_length=50,blank=False)
    content=models.TextField(blank=True)
    file = models.FileField(upload_to="practical",blank=True,null=True)
    deadline = models.DateField()

    def __str__(self):
        return self.title


class notes(models.Model):
    teacher = models.ForeignKey(teacher, on_delete=models.CASCADE)
    group = models.ForeignKey(group, on_delete=models.CASCADE)
    created = models.DateField(auto_now=True)
    title = models.CharField(max_length=50,blank=False)
    content = models.TextField(blank=True)
    file = models.FileField(upload_to="notes", blank=True, null=True)
    deadline = models.DateField()

    def __str__(self):
        return self.title