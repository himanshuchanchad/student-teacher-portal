from django.db import models
from django.contrib.auth.models import User
from home.models import group,groupmember
# Create your models here.
class teacher(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    dept=models.CharField(max_length=50)
    def __str__(self):
        return self.user.username

class assignment(models.Model):
    teacher=models.ForeignKey(teacher,on_delete=models.CASCADE)
    group=models.ForeignKey(group,on_delete=models.CASCADE)
    created = models.DateField(auto_now=True)
    div=models.CharField(max_length=10)
    dept=models.CharField(max_length=20)
    deadline=models.DateField()
    title=models.CharField(max_length=50)
    content=models.TextField(blank=False)

    def __str__(self):
        return self.title

class practical(models.Model):
    teacher=models.ForeignKey(teacher,on_delete=models.CASCADE)
    group=models.ForeignKey(group,on_delete=models.CASCADE)
    created=models.DateField(auto_now=True)
    deadline=models.DateField()
    title = models.CharField(max_length=50)
    content=models.TextField(blank=False)
    def __str__(self):
        return self.title


class notes(models.Model):
    teacher = models.ForeignKey(teacher, on_delete=models.CASCADE)
    group = models.ForeignKey(group, on_delete=models.CASCADE)
    file=models.FileField(upload_to="notes")
    created = models.DateField(auto_now=True)
    deadline = models.DateField()
    title = models.CharField(max_length=50)
    content = models.TextField(blank=False)

    def __str__(self):
        return self.title