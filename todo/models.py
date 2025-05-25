from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class TodoModel(models.Model):
    title = models.CharField(max_length=250)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    detail = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("create_todo")
