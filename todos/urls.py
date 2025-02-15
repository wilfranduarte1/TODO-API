from django.urls import path 
from .views import listTodoItem, detailTodoItem
urlpatterns = [
    path('',listTodoItem.as_view(),name='todo_list'),
    path('<int:pk>/', detailTodoItem.as_view(), name='todo_detail')
]