from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tasks
from .forms import *

# Create your views here.

def delete(request, pk):
    task = Tasks.objects.get(id = pk)

    if request.method == 'POST':
        task.delete()
        return redirect('/')
    context = {'item' : task}
    return render(request, 'tasks/delete.html', context)

def update(request, pk):
    task = Tasks.objects.get(id = pk)
    form = TasksForm(instance=task)
    if request.method == 'POST':
        form = TasksForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form' : form}
    return render(request, 'tasks/update.html', context)


def index(request):
    tasks = Tasks.objects.all()
    form = TasksForm()

    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'tasks' : tasks, 'form' : form}
    return render(request, 'tasks/index.html', context)