from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.views.generic.edit import DeleteView
from .models import TodoModel
from .forms import TodoForm
from django.urls import reverse_lazy


class CreateTodo(CreateView):
    model = TodoModel
    template_name = "todo/create.html"
    form_class = TodoForm
    success_url=reverse_lazy("list_todo")

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)


class ListTodo(ListView):
    model = TodoModel
    template_name = "todo/list.html"
    queryset=TodoModel.objects.order_by("-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = TodoForm()
        context['last_articles']=TodoModel.objects.order_by('-created_at')[:2]
        return context


class DeleteTodo(DeleteView):
    model = TodoModel
    success_url = reverse_lazy("list_todo")
