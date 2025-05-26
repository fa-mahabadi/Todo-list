from django.urls import path
from .views import CreateTodo,ListTodo,DeleteTodo,todo_search

urlpatterns=[
    path("create/",CreateTodo.as_view(),name="create_todo"),
    path("list/",ListTodo.as_view(),name="list_todo"),
    path("delete/<int:pk>/",DeleteTodo.as_view(),name="delete_todo"),
    path("search/",todo_search,name="search"),
]