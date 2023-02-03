from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

from .forms import TaskForm, LoginForm

from .models import Task


# Create your views here.
def test(request):
    return HttpResponse("<h1>Test</h1>")


class TasksView(TemplateView):
    name = "tasks"
    template = "tasks.html"

    def get(self, request, *args, **kvargs):
        if request.user.is_anonymous:
            return redirect("login")
        context = {}
        context["name"] = self.name
        tasks = Task.objects.filter(author=request.user).filter(in_list=True)
        context["tasks"] = tasks
        context["form"] = TaskForm()
        return render(request, template_name=self.template, context=context)

    def post(self, request, *args, **kvargs):
        if request.POST["action"] == "add":
            name = request.POST["name"]
            description = request.POST.get("description", "...")
            author = request.user
            Task.objects.create(
                name=name,
                description=description,
                author=author,
            )
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


class ArchiveView(TemplateView):
    name = "archive"
    template = "archive.html"

    def get(self, request, *args, **kvargs):
        if request.user.is_anonymous:
            return redirect("login")
        context = {}
        context["name"] = self.name
        tasks = Task.objects.filter(author=request.user).filter(in_list=False)
        context["tasks"] = tasks
        return render(request, template_name=self.template, context=context)

    def post(self, request, *args, **kvargs):
        id = request.POST["id"]
        if request.POST["action"] == "del":
            task = Task.objects.get(pk=id)
            task.delete()
        elif request.POST["action"] == "back":
            task = Task.objects.get(pk=id)
            task.in_list = True
            task.save()
        return redirect("archive")


class LoginView(TemplateView):
    template = "registration/login.html"

    def get(self, request, *args, **kwargs):
        if not request.user.is_anonymous:
            return redirect("tasks")
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
