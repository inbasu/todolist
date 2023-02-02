from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    name = forms.CharField(required=True, label=False)
    description = forms.CharField(label=False)

    name.widget.attrs.update({"id": "name-form"})

    class Meta:
        model = Task
        exclude = ("in_list",)
