from django.urls import path

from . import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("start/", views.start_task_view, name="start_task"),
    path("logs/", views.logs_page_view, name="logs_page"),  # <-- именно /logs/
    path("logs/data/", views.logs_data_view, name="get_logs"),
]
