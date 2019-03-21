from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class group(models.Model):
    name=models.CharField(max_length=256,unique=True)
    member=models.ManyToManyField(User,through="groupmember")
    sub = models.CharField(max_length=256)
    div_or_batch=models.CharField(max_length=50)
    div=models.BooleanField(default=False)
    batch=models.BooleanField(default=False)
    year=models.CharField(max_length=256)
    dept=models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def students_member(self):
        pass

class groupmember(models.Model):
    group=models.ForeignKey(group,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class teacher(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=256,unique=False)
    dept=models.CharField(max_length=50)
    def __str__(self):
        return self.user.username

class student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    sapid=models.PositiveIntegerField(blank=False)
    year=models.CharField(blank=False, max_length=20)
    div=models.CharField(blank=False , max_length=20)
    batch=models.CharField(blank=False, max_length=20)
    dept=models.CharField(blank=False, max_length=20)
    def __str__(self):
        return self.user.username

class assignment(models.Model):
    teacher=models.ForeignKey(teacher,on_delete=models.CASCADE)
    group=models.ForeignKey(group,on_delete=models.CASCADE)
    sub=models.CharField(max_length=256)
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
    deadline = models.DateField()
    title = models.CharField(max_length=50)
    content = models.TextField(blank=False)

    def __str__(self):
        return self.title