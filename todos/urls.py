from django.urls import path 
from .views import listTodoItem
urlpatterns = [
    path('',listTodoItem.as_view(),name='todo_list'),
]