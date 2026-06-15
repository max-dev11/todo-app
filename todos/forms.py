"""Forms for the todos app."""
from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    """Form for creating and updating tasks."""

    class Meta:
        model = Task
        fields = ["title", "description", "priority"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "priority": forms.Select(attrs={"class": "form-select"}),
        }
