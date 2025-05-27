from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView,UpdateView
from .models import TodoModel
from .forms import TodoForm
from django.urls import reverse_lazy


class CreateTodo(LoginRequiredMixin,CreateView):
    model = TodoModel
    template_name = "todo/create.html"
    form_class = TodoForm
    success_url=reverse_lazy("list_todo")

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)


class ListTodo(LoginRequiredMixin,ListView):
    model = TodoModel
    template_name = "todo/list.html"

    def get_queryset(self):
        return TodoModel.objects.filter(author=self.request.user).order_by("-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = TodoForm()
        context['last_articles']=TodoModel.objects.filter(author=self.request.user).order_by('-created_at')[:2]
        return context
    
class UpdateTodo(LoginRequiredMixin,UpdateView):
    model=TodoModel
    fields=("title","detail")
    success_url=reverse_lazy("list_todo")
    template_name="todo/update.html"

class DeleteTodo(LoginRequiredMixin,DeleteView):
    model = TodoModel
    success_url = reverse_lazy("list_todo")


@login_required
def todo_search(request):
    query=request.GET.get("q")
    qs=TodoModel.objects.filter(title__contains=query , author=request.user)
    return render(request,"todo/result.html",context={"todos":qs})