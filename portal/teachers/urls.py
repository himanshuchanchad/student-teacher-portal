from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.teachersignup,name='signup'),
    path('',views.teacher_login,name="login"),

]