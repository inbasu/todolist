from django import forms
from django.contrib.auth.models import User
from .models import Task


class TaskForm(forms.ModelForm):
    name = forms.CharField(required=True, label=False)
    description = forms.CharField(label=False)

    name.widget.attrs.update({"id": "name-form"})

    class Meta:
        model = Task
        exclude = ("in_list",)


class LoginForm(forms.ModelForm):
    username = forms.CharField(required=True, label=False)
    password = forms.CharField(required=True, label=False)

    class Meta:
        model = User
        fields = ["username", "password"]
