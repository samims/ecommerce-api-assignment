from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm


class SignupView(CreateView):
    form_class = SignUpForm

