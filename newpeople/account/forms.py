from django.contrib.auth.forms import (UserCreationForm, UserChangeForm)
from .models import CustomUser
from django import forms
 
class CustomUserCreationForm(UserCreationForm):
 
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'gender', 'area', 'keyword')
 
 
class CustomUserChangeForm(UserChangeForm):
 
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'gender', 'area', 'keyword')
