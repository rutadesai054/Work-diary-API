from django.urls import path
from .views import *

urlpatterns = [
    path('',taskListAPI,name='taskListAPI'),
    path('taskDetailAPI/<int:task_id>', taskDetailAPI, name='taskDetailAPI'),

]

# Create your tests here.
