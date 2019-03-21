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



