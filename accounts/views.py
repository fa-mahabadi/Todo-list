from django.shortcuts import render
from .forms import RegisterForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

class SignUp(CreateView):
    form_class=RegisterForm
    template_name="registration/SignUp.html"
    success_url=reverse_lazy("login")