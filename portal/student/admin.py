from django.contrib import admin
from .models import students,student_practical,student_assignment
# Register your models here.
admin.site.register(students)
admin.site.register(student_assignment)
admin.site.register(student_practical)