from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.teachersignup,name='signup'),
    path('',views.teacher_login,name="login"),
    path('teacher_home/',views.teacher_home,name='teacher_home'),
    path('addassignment/<int:pk>/',views.addassignment,name='addassignment'),
    path('addpractical/<int:pk>/',views.addpractical,name='addpractical'),
    path('addnotes/<int:pk>/',views.addnotes,name='addnotes'),
    path('viewassignment/<int:assignpk>/',views.viewassignment,name='viewassignment'),
    path('viewpractical/<int:assignpk>/', views.viewpractical, name='viewpractical'),
    path('viewnotes/<int:assignpk>/', views.viewnotes, name='viewnotes'),
    path('teacher_view_all/<int:pk>/<slug:type>/',views.teacher_view_all,name='teacher_view_all'),
]