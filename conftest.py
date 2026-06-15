"""Pytest configuration and fixtures."""
import pytest
from django.urls import reverse


@pytest.fixture
def task_list_url():
    """Return the task list URL."""
    return reverse("todos:task_list")


@pytest.fixture
def task_create_url():
    """Return the task create URL."""
    return reverse("todos:task_create")
