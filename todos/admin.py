"""Admin configuration for the todos app."""
from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """Admin interface for Task model."""

    list_display = ["title", "priority", "completed", "created_at", "completed_at"]
    list_filter = ["priority", "completed", "created_at"]
    search_fields = ["title", "description"]
    list_editable = ["priority", "completed"]
    readonly_fields = ["created_at", "updated_at", "completed_at"]
    ordering = ["-created_at"]
