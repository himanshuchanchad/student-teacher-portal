from django.urls import path
from . import views

urlpatterns=[
    path('signup/', views.studentsignup, name='signup'),
    path('', views.student_login, name="login"),
    path('student_home/', views.student_home,name='student_home'),
    path('submitassignment/<int:pk>/<int:assignpk>' ,views.submitassignment,name='submitassignment'),
    path('submitpractical/<int:pk>/<int:assignpk>' ,views.submitpractical,name='submitpractical'),
    path('joingroups/<int:pk>/',views.joingroups,name='joingroups')
]