from django.shortcuts import render, redirect
from main.models import Task
from main.forms import TaskForm
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    task = Task.objects.filter(user=request.user)
    context = {"task": task}
    return render(request, "main/home.html", context)


def delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect("home")


def update(request, id):
    task = Task.objects.get(id=id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TaskForm(instance=task)

    context = {
        "edit": task,
        "form": form,
    }
    return render(request, "main/edit.html", context)


def create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(False)
            task.user = request.user
            task.save()
            return redirect("home")
    else:
        form = TaskForm()

    context = {
        "form": form,
    }
    return render(request, "main/create.html", context)
