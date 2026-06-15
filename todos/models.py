"""Models for the todos app."""
from django.db import models
from django.utils import timezone


class Task(models.Model):
    """Represents a to-do task."""

    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="")
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default="medium")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def mark_complete(self):
        """Mark the task as complete."""
        self.completed = True
        self.completed_at = timezone.now()
        self.save()

    def mark_incomplete(self):
        """Mark the task as incomplete."""
        self.completed = False
        self.completed_at = None
        self.save()
