from django.shortcuts import render,redirect
from .forms import taskForm
from .models import Task
from category.models import Category

def task(req):
    task = Task.objects.all()
    return render (req,'task/show.html',{'data':task})

def add_task(req):
    if req.method == 'POST':
        form = taskForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('task')
    else:
        form = taskForm()
    return render (req,'task/task.html',{'form':form})

def edit_task(req,id):
    task = Task.objects.get(pk = id)
    form = taskForm(instance=task)
    if req.method == 'POST':
        form = taskForm(req.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('task')
    return render (req,'task/edit.html',{'form':form})

def delete(req,id):
    task = Task.objects.get(pk = id)
    task.delete()
    return redirect('task')
