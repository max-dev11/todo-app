"""Tests for the todos app."""
import pytest
from django.urls import reverse
from django.utils import timezone

from todos.models import Task


@pytest.mark.django_db
class TestTaskModel:
    """Tests for the Task model."""

    def test_create_task(self):
        """Test creating a task."""
        task = Task.objects.create(
            title="Test Task",
            description="Test Description",
            priority="high",
        )
        assert task.pk is not None
        assert task.title == "Test Task"
        assert task.description == "Test Description"
        assert task.priority == "high"
        assert task.completed is False
        assert task.completed_at is None

    def test_task_str(self):
        """Test task string representation."""
        task = Task.objects.create(title="My Task")
        assert str(task) == "My Task"

    def test_task_ordering(self):
        """Test that tasks are ordered by created_at descending."""
        task1 = Task.objects.create(title="First")
        task2 = Task.objects.create(title="Second")
        tasks = list(Task.objects.all())
        assert tasks[0] == task2
        assert tasks[1] == task1

    def test_mark_complete(self):
        """Test marking a task as complete."""
        task = Task.objects.create(title="Complete Me")
        assert task.completed is False
        task.mark_complete()
        assert task.completed is True
        assert task.completed_at is not None

    def test_mark_incomplete(self):
        """Test marking a task as incomplete."""
        task = Task.objects.create(title="Incomplete Me", completed=True)
        task.completed_at = timezone.now()
        task.save()
        task.mark_incomplete()
        assert task.completed is False
        assert task.completed_at is None

    def test_task_default_values(self):
        """Test default values for task fields."""
        task = Task.objects.create(title="Default Task")
        assert task.description == ""
        assert task.priority == "medium"
        assert task.completed is False


@pytest.mark.django_db
class TestTaskViews:
    """Tests for the task views."""

    def test_task_list_view(self, client):
        """Test the task list view."""
        Task.objects.create(title="Task 1")
        Task.objects.create(title="Task 2")
        response = client.get(reverse("todos:task_list"))
        assert response.status_code == 200
        assert "tasks" in response.context
        assert len(response.context["tasks"]) == 2

    def test_task_list_filter_active(self, client):
        """Test filtering to show only active tasks."""
        Task.objects.create(title="Active Task")
        Task.objects.create(title="Completed Task", completed=True)
        response = client.get(f"{reverse('todos:task_list')}?filter=active")
        assert response.status_code == 200
        assert len(response.context["tasks"]) == 1
        assert response.context["tasks"][0].title == "Active Task"

    def test_task_list_filter_completed(self, client):
        """Test filtering to show only completed tasks."""
        Task.objects.create(title="Active Task")
        Task.objects.create(title="Completed Task", completed=True)
        response = client.get(f"{reverse('todos:task_list')}?filter=completed")
        assert response.status_code == 200
        assert len(response.context["tasks"]) == 1
        assert response.context["tasks"][0].title == "Completed Task"

    def test_task_list_filter_priority(self, client):
        """Test filtering by priority."""
        Task.objects.create(title="High Priority", priority="high")
        Task.objects.create(title="Low Priority", priority="low")
        response = client.get(f"{reverse('todos:task_list')}?priority=high")
        assert response.status_code == 200
        assert len(response.context["tasks"]) == 1
        assert response.context["tasks"][0].priority == "high"

    def test_task_create_view_get(self, client):
        """Test the task create view (GET)."""
        response = client.get(reverse("todos:task_create"))
        assert response.status_code == 200
        assert "form" in response.context

    def test_task_create_view_post(self, client):
        """Test creating a task via POST."""
        response = client.post(
            reverse("todos:task_create"),
            {"title": "New Task", "description": "New Description", "priority": "high"},
        )
        assert response.status_code == 302  # Redirect after success
        assert Task.objects.filter(title="New Task").exists()

    def test_task_update_view_get(self, client):
        """Test the task update view (GET)."""
        task = Task.objects.create(title="Update Me")
        response = client.get(reverse("todos:task_update", args=[task.pk]))
        assert response.status_code == 200
        assert "form" in response.context
        assert response.context["task"] == task

    def test_task_update_view_post(self, client):
        """Test updating a task via POST."""
        task = Task.objects.create(title="Old Title")
        response = client.post(
            reverse("todos:task_update", args=[task.pk]),
            {"title": "New Title", "description": "", "priority": "low"},
        )
        assert response.status_code == 302
        task.refresh_from_db()
        assert task.title == "New Title"

    def test_task_delete_view_get(self, client):
        """Test the task delete confirmation view (GET)."""
        task = Task.objects.create(title="Delete Me")
        response = client.get(reverse("todos:task_delete", args=[task.pk]))
        assert response.status_code == 200
        assert "task" in response.context

    def test_task_delete_view_post(self, client):
        """Test deleting a task via POST."""
        task = Task.objects.create(title="Delete Me")
        response = client.post(reverse("todos:task_delete", args=[task.pk]))
        assert response.status_code == 302
        assert not Task.objects.filter(pk=task.pk).exists()

    def test_task_toggle_complete(self, client):
        """Test toggling a task to complete."""
        task = Task.objects.create(title="Toggle Me", completed=False)
        response = client.post(reverse("todos:task_toggle", args=[task.pk]))
        assert response.status_code == 302
        task.refresh_from_db()
        assert task.completed is True

    def test_task_toggle_incomplete(self, client):
        """Test toggling a task to incomplete."""
        task = Task.objects.create(title="Toggle Me", completed=True)
        response = client.post(reverse("todos:task_toggle", args=[task.pk]))
        assert response.status_code == 302
        task.refresh_from_db()
        assert task.completed is False

    def test_task_clear_completed(self, client):
        """Test clearing all completed tasks."""
        Task.objects.create(title="Keep Me")
        Task.objects.create(title="Delete Me", completed=True)
        response = client.post(
            reverse("todos:task_clear_completed"),
            HTTP_REFERER=reverse("todos:task_list"),
        )
        assert response.status_code == 302
        assert Task.objects.filter(completed=True).count() == 0
        assert Task.objects.filter(completed=False).count() == 1

    def test_stats_in_context(self, client):
        """Test that stats are included in the context."""
        Task.objects.create(title="Task 1", completed=True)
        Task.objects.create(title="Task 2")
        response = client.get(reverse("todos:task_list"))
        assert "stats" in response.context
        assert response.context["stats"]["total"] == 2
        assert response.context["stats"]["completed"] == 1
        assert response.context["stats"]["active"] == 1


@pytest.mark.django_db
class TestTaskForm:
    """Tests for the TaskForm."""

    def test_form_valid(self):
        """Test form validation with valid data."""
        from todos.forms import TaskForm
        form = TaskForm(data={"title": "Valid Task", "priority": "high"})
        assert form.is_valid()

    def test_form_invalid_empty_title(self):
        """Test form validation with empty title."""
        from todos.forms import TaskForm
        form = TaskForm(data={"title": "", "priority": "high"})
        assert not form.is_valid()
        assert "title" in form.errors

    def test_form_invalid_long_title(self):
        """Test form validation with title exceeding max length."""
        from todos.forms import TaskForm
        form = TaskForm(data={"title": "x" * 201, "priority": "high"})
        assert not form.is_valid()
        assert "title" in form.errors
