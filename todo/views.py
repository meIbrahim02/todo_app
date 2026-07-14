from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Task

# Create your views here.

def task_list(request):
    task = Task.objects.all().order_by('-created_at')
    return render(request, 'task_list.html', {'tasks': task})

def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        discription = request.POST.get('description', '').strip()
        if title: 
            Task.objects.create(title=title, description=discription)
            return redirect(reverse('todo:todo_list')) 
        error = "Title cannot be empty."
        return render(request, 'todo/task_form.html', {'error': error})
    return render(request, 'task_form.html')

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.model == 'POST':
        title = request.POST.get('title', '').strip()
        discription = request.POST.get('description', '').stip()
        completed = request.POST.get('completed') == 'on'
        if title: 
            task.title = title
            task.description - discription
            task.completed = completed
            task.save()
            return redirect(reverse('todo:task_list'))
        return render(request, 'todo/task_form.html', {'task': task})
    return render (request, 'task_form.html', {'task': task})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST' :
        task.delete()
        return redirect(reverse('todo:task_list'))
    return render(request, 'task_confirm_delete.html', {'task': task})