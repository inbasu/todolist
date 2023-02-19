from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import TaskForm, LoginForm

from .models import Task


# Create your views here.
def test(request):
    return HttpResponse("<h1>Test</h1>")


class TasksView(LoginRequiredMixin, TemplateView):
    name = "tasks"
    template = "tasks.html"

    def get(self, request, *args, **kvargs):
        tasks = Task.objects.filter(author=request.user).filter(in_list=True)
        context = {}
        context["name"] = self.name
        context["tasks"] = tasks
        context["form"] = TaskForm()
        return render(request, template_name=self.template, context=context)

    def post(self, request, *args, **kvargs):
        if request.POST["action"] == "add":
            form = TaskForm(request.POST)
            if form.is_valid():
                task = form.save(commit=False)
                task.author = request.user
                task.save()

        elif request.POST["action"] == "done-undone":
            id = request.POST["id"]
            task = Task.objects.get(pk=id)
            task.done_undone()

        elif request.POST["action"] == "clear-list":
            for task in Task.objects.filter(author=request.user).filter(in_list=True):
                if task.done:
                    task.in_list = False
                    task.save()
        return redirect("tasks")


class ArchiveView(LoginRequiredMixin, TemplateView):
    name = "archive"
    template = "archive.html"

    def get(self, request, *args, **kvargs):
        context = {}
        context["name"] = self.name
        tasks = Task.objects.filter(author=request.user).filter(in_list=False)
        context["tasks"] = tasks
        return render(request, template_name=self.template, context=context)

    def post(self, request, *args, **kvargs):
        id = request.POST["id"]
        if request.POST["action"] == "del":
            try:
                task = Task.objects.get(pk=id, author=request.user)
                task.delete()
            except:
                return redirect("archive")
        elif request.POST["action"] == "back":
            task = Task.objects.get(pk=id)
            task.in_list = True
            task.save()
        return redirect("archive")


class LoginView(TemplateView):
    template = "registration/login.html"

    def get(self, request, *args, **kwargs):
        context = {}
        context["name"] = "Login"
        form = LoginForm()
        context["form"] = form
        return render(request, template_name=self.template, context=context)

    def post(self, request, *args, **kwargs):
        user = authenticate(
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is not None:
            login(request, user)
            return redirect("tasks")
        return redirect("login")
