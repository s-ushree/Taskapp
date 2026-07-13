from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form, 'title': 'Create Task'})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        print("UPDATE POST request received")
        print("FILES:", request.FILES)
        print("POST data:", request.POST)

        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            print("Update form is valid")
            task = form.save()
            print("Task updated:", task)
            messages.success(request, 'Task updated successfully!')
            return redirect('task_list')
        else:
            print("Update form errors:", form.errors)
            messages.error(request, 'Please correct the errors below.')
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/task_form.html', {'form': form, 'title': 'Update Task'})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully!')
        return redirect('task_list')

    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

# Create your views here.
