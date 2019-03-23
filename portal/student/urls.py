from django.urls import path
from . import views

urlpatterns=[
    path('signup/', views.studentsignup, name='signup'),
    path('', views.student_login, name="login"),
    path('student_home/', views.student_home,name='student_home')
]