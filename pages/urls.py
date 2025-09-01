from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("start/", views.start_task, name="start_task"),
    path("logs/task/", views.logs_view, name="logs"),  # Отображение логов выполнения задачи
    path("logs/data/", views.get_logs, name="get_logs"),  # Получение логов выполнения задачи
]
