from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

dept_choices = (
    ('computer engineering', 'computer engineering'),
    ('it engineering', 'it engineering'),
    ('production engineering', 'production engineering'),
    ('mechanical engineering', 'mechanical engineering'),
    ('chemical engineering', 'chemical engineering'),
    ('bio-med engineering', 'bio-med engineering')
)
div_choices = (
    ('A', 'A'),
    ('B', 'B'),
)
batch_choices = (
    ('A1', 'A1'),
    ('A2', 'A2'),
    ('A3', 'A3'),
    ('A4', 'A4'),
    ('B1', 'B1'),
    ('B2', 'B2'),
    ('B3', 'B3'),
    ('B4', 'B4'),

)
year_choices = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
)

class teacher(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    dept=models.CharField(choices=dept_choices,max_length=200,blank=True)

    def __str__(self):
        return self.user.username

class students(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    sapid=models.PositiveIntegerField(blank=False)
    year=models.CharField(blank=False, max_length=20,choices=year_choices)
    div=models.CharField(max_length=20,choices=div_choices)
    batch=models.CharField(blank=False, max_length=20,choices=batch_choices)
    dept=models.CharField(choices=dept_choices, max_length=20)

    def __str__(self):
        return self.user.username


class group(models.Model):
    owner=models.ForeignKey(teacher,on_delete=models.CASCADE)
    name=models.CharField(max_length=256,null=False,blank=False)
    member=models.ManyToManyField(students)
    sub = models.CharField(max_length=256 ,null=False,blank=False)
    division=models.CharField(max_length=50,choices=div_choices)
    batch=models.CharField(max_length=50,blank=True,null=True,choices=batch_choices)
    div=models.BooleanField(default=False)
    batch_check=models.BooleanField(default=False)
    year=models.CharField(max_length=256,choices=year_choices)
    dept=models.CharField(max_length=256,choices=dept_choices)

    def __str__(self):
        return self.name

# def post_save_group(sender,instance,*args,**kwargs):
#     create_groupmember=instance
#     if instance.member is None:
#         if sender.div :
#             student=students.objects.filter(div=instance.div_or_batch)
#             for s in student :
#                 create_groupmember.member.add(s)
#                 create_groupmember.save()
#
#         elif sender.batch:
#             student = students.objects.filter(batch=instance.div_or_batch)
#             print(student)
#             for s in student:
#                 create_groupmember.member.add(s)
#                 create_groupmember.save()
#
# post_save.connect(post_save_group,sender=group)

# class groupmember(models.Model):
#     group=models.ForeignKey(group,on_delete=models.CASCADE)
#     user=models.ManyToManyField('students')
#
#     def __str__(self):
#         return f"{group.name}"



