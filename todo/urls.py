from django.contrib import admin
from django.urls import path, include

from .views import TasksView, ArchiveView, LoginView

urlpatterns = [
    path("", TasksView.as_view(), name="tasks"),
    path("arch/", ArchiveView.as_view(), name="archive"),
    path("login/", LoginView.as_view(), name="login"),
]
