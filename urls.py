from django.contrib import admin
from django.urls import path
from . import views
from demoapp.views import *
urlpatterns = [

    # Student Functions
    path('student_list', views.student_list, name='student_list'),
    path('delete_student/<int:id>/', views.delete_student,name='delete_student'),
    path('update_student/<int:id>/', views.update_student, name='update_student'),
    path('add_student', views.add_student, name='add_student'),

]    
    
