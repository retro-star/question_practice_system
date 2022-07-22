from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.begin),
    # 登陆、注册、注销
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    # 管理员
    path('admin/', views.admin),
    path('admin/add/', views.admin_add),
    path('admin/<int:nid>/edit/', views.admin_edit),
    path('admin/delete/', views.admin_delete),
    path('admin/course/', views.admin_course),
    # 老师
    path('teacher/', views.teacher),
    path('teacher/delete/', views.teacher_delete),
    path('teacher/add/', views.teacher_add),
    # 题目
    path('question/', views.question),
    path('choice/', views.choice_add),
    path('choice/delete/', views.choice_delete),
    path('tf/', views.tf_add),
    path('tf/delete/', views.tf_delete),
    path('com/', views.com_add),
    path('com/delete', views.com_delete),
    # 学生
    path('student/', views.student),
    path('student/add/', views.student_add),
    path('test/', views.test),
    path('test/cho_anw/', views.cho_anw),
    path('test/tf_anw/', views.tf_anw),
    path('test/com_anw/', views.com_anw),
    path('student/grade/', views.grade),
    path('student/grade/all/', views.grade_all),
    path('student/grade/choice/', views.grade_choice),
    path('student/grade/tf/', views.grade_tf),
    path('student/grade/com/', views.grade_com),
]
