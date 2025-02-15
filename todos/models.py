from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    body =models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    update = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
