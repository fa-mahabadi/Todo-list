from django.urls import path
from .views import CreateTodo,ListTodo,DeleteTodo

urlpatterns=[
    path("create/",CreateTodo.as_view(),name="create_todo"),
    path("list/",ListTodo.as_view(),name="list_todo"),
    path("delete/<int:pk>/",DeleteTodo.as_view(),name="delete_todo")
]