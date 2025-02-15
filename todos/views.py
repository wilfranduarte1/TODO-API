from .models import TodoItem
from .sereializers import TodoItemSerializer
from rest_framework import generics

# Create your views here.
class listTodoItem(generics.ListAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer