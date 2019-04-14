from django import template
from student.models import student_assignment
register = template.Library()
from home.models import students
@register.simple_tag(name='check')
def studentcheck(**kwargs):
    user=kwargs['user']
    assignment=kwargs['assignment']
    student=students.objects.get(user=user)
    try:
        check_student_assignment=student_assignment.objects.filter(student=student,assignment=assignment)
        if check_student_assignment:
            return True
    except:
        return False

# @register.inclusion_tag(name='check',takes_context=True)
# def studentcheck(**kwargs):
#     user=kwargs['user']
#     assignment=kwargs['assignment']
#     student=students.objects.get(user=user)
#     try:
#         check_student_assignment=student_assignment.objects.filter(student=student,assignment=assignment)
#         if check_student_assignment:
#             return True
#     except:
#         return False