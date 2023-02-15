from django import forms
from django.contrib.auth.models import User
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name"]


class LoginForm(forms.ModelForm):
    username = forms.CharField(required=True, label=False)
    password = forms.CharField(required=True, label=False)

    class Meta:
        model = User
        fields = ["username", "password"]
