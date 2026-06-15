"""Views for the todos app."""
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TaskForm
from .models import Task


def task_list(request):
    """Display all tasks with optional filtering."""
    filter_status = request.GET.get("filter", "all")
    filter_priority = request.GET.get("priority", "all")

    tasks = Task.objects.all()

    if filter_status == "active":
        tasks = tasks.filter(completed=False)
    elif filter_status == "completed":
        tasks = tasks.filter(completed=True)

    if filter_priority != "all":
        tasks = tasks.filter(priority=filter_priority)

    context = {
        "tasks": tasks,
        "filter_status": filter_status,
        "filter_priority": filter_priority,
        "stats": {
            "total": Task.objects.count(),
            "completed": Task.objects.filter(completed=True).count(),
            "active": Task.objects.filter(completed=False).count(),
        },
    }
    return render(request, "todos/task_list.html", context)


def task_create(request):
    """Create a new task."""
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Task created successfully!")
            return redirect("todos:task_list")
    else:
        form = TaskForm()

    return render(request, "todos/task_form.html", {"form": form, "action": "Create"})


def task_update(request, pk):
    """Update an existing task."""
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully!")
            return redirect("todos:task_list")
    else:
        form = TaskForm(instance=task)

    return render(request, "todos/task_form.html", {"form": form, "task": task, "action": "Update"})


def task_delete(request, pk):
    """Delete a task."""
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        task.delete()
        messages.success(request, "Task deleted successfully!")
        return redirect("todos:task_list")

    return render(request, "todos/task_confirm_delete.html", {"task": task})


def task_toggle(request, pk):
    """Toggle task completion status."""
    task = get_object_or_404(Task, pk=pk)

    if task.completed:
        task.mark_incomplete()
        messages.info(request, "Task marked as incomplete.")
    else:
        task.mark_complete()
        messages.success(request, "Task completed!")

    return redirect("todos:task_list")


def task_clear_completed(request):
    """Delete all completed tasks."""
    if request.method == "POST":
        deleted_count, _ = Task.objects.filter(completed=True).delete()
        messages.success(request, f"Deleted {deleted_count} completed task(s).")
    return redirect("todos:task_list")
