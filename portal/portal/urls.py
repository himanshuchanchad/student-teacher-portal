"""portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path('',views.index,name='index'),
    path('admin/', admin.site.urls),
    path('create/',views.create_group,name="create_group"),
    path('teacher/',include(('teachers.urls',' teacher'),namespace='teacher')),
    path('student/',include(('student.urls','student'),namespace='student')),
    path('logout/',views.logoutrequest,name='request_logout'),
    path('teacher_group_detail/<int:pk>/',views.teacher_group_detail,name="teacher_group_detail"),
    path('student_group_detail/<int:pk>/',views.student_group_detail,name="student_group_detail"),
]
