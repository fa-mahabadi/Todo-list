from django.shortcuts import render
from django.views.generic import CreateView
from .models import TodoModel
from .forms import TodoForm

class CreateTodo(CreateView):
    model=TodoModel
    template_name="todo/create.html"
    form_class=TodoForm