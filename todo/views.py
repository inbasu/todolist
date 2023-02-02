from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import TaskForm
from .models import Task


# Create your views here.
def test(request):
    return HttpResponse("<h1>Test</h1>")


class TaskView(TemplateView):
    template = "tasks.html"

    def get(self, request, *args, **kvargs):
        context = {}
        tasks = Task.objects.filter(in_list=True)
        context["tasks"] = tasks
        context["form"] = TaskForm()
        return render(request, template_name=self.template, context=context)

    def post(self, request, *args, **kvargs):
        if request.POST["action"] == "add":
            name = request.POST["name"]
            description = request.POST.get("description", "...")
            Task.objects.create(name=name, description=description)
        elif request.POST["action"] == "del":
            id = request.POST["id"]
            task = Task.objects.get(pk=id)
            task.done_undone()
        elif request.POST["action"] == "clear-all":
            for task in Task.objects.filter(in_list=True):
                if task.done:
                    task.in_list = False
                    task.save()
        return redirect("tasks")


class ArchiveView(TemplateView):
    template = "archive.html"

    def get(self, request, *args, **kvargs):
        context = {}
        tasks = Task.objects.filter(in_list=False)
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
