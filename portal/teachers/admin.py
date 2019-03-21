from django.contrib import admin
from .models import teacher,notes,assignment,practical
# Register your models here.
admin.site.register(teacher)
admin.site.register(notes)
admin.site.register(assignment)
admin.site.register(practical)