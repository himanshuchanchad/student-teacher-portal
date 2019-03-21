from django.db import models
from django.contrib.auth.models import User
from teachers.models import assignment,practical
# Create your models here.
class student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    sapid=models.PositiveIntegerField(blank=False)
    year=models.CharField(blank=False, max_length=20)
    div=models.CharField(blank=False , max_length=20)
    batch=models.CharField(blank=False, max_length=20)
    dept=models.CharField(blank=False, max_length=20)
    def __str__(self):
        return self.user.username


class student_assignment(models.Model):
    student=models.ForeignKey(student,on_delete=models.CASCADE)
    assignment=models.ForeignKey(assignment,on_delete=models.CASCADE)
    file=models.FileField(upload_to="assignment/")
    submission=models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.student} {self.assignment.title}"

class student_practical(models.Model):
    student=models.ForeignKey(student,on_delete=models.CASCADE)
    practical=models.ForeignKey(practical,on_delete=models.CASCADE)
    file=models.FileField(upload_to="practical/")
    submission=models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.student} {self.practical.title}"