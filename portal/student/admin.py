from django.contrib import admin
from .models import student,student_practical,student_assignment
# Register your models here.
admin.site.register(student)
admin.site.register(student_assignment)
admin.site.register(student_practical)