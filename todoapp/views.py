from django.shortcuts import render, redirect

from .models import Task
from .forms import AddTaskForm

def index(req):
    # Formulaire d'ajout d'une tâche
    if req.method != 'POST':
        form = AddTaskForm()
    else:
        form = AddTaskForm(req.POST)
        if form.is_valid():
            Task.objects.create(title=form.cleaned_data["title"])
            return redirect("index")

    task_list = Task.objects.all()
    
    context = {
        "task_list": task_list,
        "form"     : form
    }

    return render(req, "todoapp/index.html", context)

def complete(req, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = False if task.completed else True
    task.save()
    return redirect("index")

def remove(req, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect("index")