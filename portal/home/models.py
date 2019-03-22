from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save


class teacher(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    dept=models.CharField(max_length=50)
    def __str__(self):
        return self.user.username

class students(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    sapid=models.PositiveIntegerField(blank=False)
    year=models.CharField(blank=False, max_length=20)
    div=models.CharField(blank=False , max_length=20)
    batch=models.CharField(blank=False, max_length=20)
    dept=models.CharField(blank=False, max_length=20)
    def __str__(self):
        return self.user.username


class group(models.Model):
    owner=models.OneToOneField(teacher,on_delete=models.CASCADE)
    name=models.CharField(max_length=256,unique=True)
    member=models.ManyToManyField(students)
    sub = models.CharField(max_length=256)
    div_or_batch=models.CharField(max_length=50)
    div=models.BooleanField(default=False)
    batch=models.BooleanField(default=False)
    year=models.CharField(max_length=256)
    dept=models.CharField(max_length=256)

    def __str__(self):
        return self.name

def pre_save_group(sender,instance,*args,**kwargs):
    create_groupmember=sender
    if sender.div :
        student=students.objects.filter(div=sender.div_or_batch)
        for s in student :
            create_groupmember.add(s)

    elif sender.batch:
        student = students.objects.filter(batch=sender.div_or_batch)
        for s in student:
            create_groupmember.add(s)
        create_groupmember.save()

pre_save.connect(pre_save_group,sender=group)

# class groupmember(models.Model):
#     group=models.ForeignKey(group,on_delete=models.CASCADE)
#     user=models.ManyToManyField('students')
#
#     def __str__(self):
#         return f"{group.name}"



