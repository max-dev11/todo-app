"""URL configuration for the todos app."""
from django.urls import path

from . import views

app_name = "todos"

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("create/", views.task_create, name="task_create"),
    path("update/<int:pk>/", views.task_update, name="task_update"),
    path("delete/<int:pk>/", views.task_delete, name="task_delete"),
    path("toggle/<int:pk>/", views.task_toggle, name="task_toggle"),
    path("clear-completed/", views.task_clear_completed, name="task_clear_completed"),
]
