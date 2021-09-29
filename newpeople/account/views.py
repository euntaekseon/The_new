from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
 
from .forms import CustomUserCreationForm

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, get_user_model


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('signup_success')
    template_name = 'account/signup.html'
