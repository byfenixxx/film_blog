from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import *


class RegisterView(SuccessMessageMixin, CreateView):
    model = User
    template_name = "account/register.html"
    form_class = RegistrationForm
    success_url = reverse_lazy("index")
    success_message = "Successfully registered"


class SignInView(LoginView):
    template_name = "account/login.html"


def profile(request):
    return render(request, "account/profile.html")
