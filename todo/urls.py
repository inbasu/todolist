from django.contrib import admin
from django.urls import path

from .views import TaskView, ArchiveView

urlpatterns = [
    path("", TaskView.as_view(), name="tasks"),
    path("arch/", ArchiveView.as_view(), name="archive"),
]
