from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.teachersignup,name='signup'),
    path('',views.teacher_login,name="login"),
    path('teacher_home/',views.teacher_home,name='teacher_home'),
    path('addassignment/<int:pk>/',views.addassignment,name='addassignment'),
    path('addpractical/<int:pk>/',views.addpractical,name='addpractical'),
    path('addnotes/<int:pk>/',views.addnotes,name='addnotes'),

]