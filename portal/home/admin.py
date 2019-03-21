from django.contrib import admin
from .models import student,teacher,notes,assignment,practical,group,groupmember
# Register your models here.
admin.site.register(student)
admin.site.register(teacher)
admin.site.register(notes)
admin.site.register(assignment)
admin.site.register(practical)
admin.site.register(group)
admin.site.register(groupmember)