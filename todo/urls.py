from django.urls import path
from .views import CreateTodo

urlpatterns=[
    path("create/",CreateTodo.as_view(),name="create_todo"),
]