from django.db import models
from django.contrib.auth.models import User
from teachers.models import assignment,practical
from home.models import group,students
# Create your models here.


class student_assignment(models.Model):
    student=models.ForeignKey(students,on_delete=models.CASCADE)
    group=models.ForeignKey(group,on_delete=models.CASCADE)
    assignment=models.ForeignKey(assignment,on_delete=models.CASCADE)
    submission=models.DateField(auto_now=True)
    file = models.FileField(upload_to="assignment")

    def __str__(self):
        return f"{self.student} {self.assignment.title}"

class student_practical(models.Model):
    student=models.ForeignKey(students,on_delete=models.CASCADE)
    group = models.ForeignKey(group, on_delete=models.CASCADE)
    practical=models.ForeignKey(practical,on_delete=models.CASCADE)
    submission=models.DateField(auto_now=True)
    file = models.FileField(upload_to="practical")

    def __str__(self):
        return f"{self.student} {self.practical.title}"