"""homework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from blog.views import index, view_comments, view_comments_start_middle_finish, change_comments_start_middle_finish, delete_k_objects, get_last_two_objects
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('comments', view_comments, name='comments'),
    path('task2', view_comments_start_middle_finish, name='task2'),
    path('task3', change_comments_start_middle_finish, name='task3'),
    path('task5', delete_k_objects, name='task5'),
    path('task6', get_last_two_objects, name='task6')
]
