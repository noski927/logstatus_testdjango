from django.core.cache import cache
from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect, render

from pages.tasks import long_process_task


def index_view(request: HttpRequest) -> render:
    """
    Отображает основную страницу приложения с формой
    """
    status = request.GET.get("status")
    return render(request, "pages/index.html", {"status": status})


def start_task_view(request):
    if request.method == "POST":
        seconds = int(request.POST.get("seconds", 5))

        task = long_process_task.delay(seconds)

        # перенаправляем на логи задачи
        return redirect(f"/logs/?task_id={task.id}")

    return redirect("index")


def logs_page_view(request: HttpRequest) -> render:
    """
    Отображение логов выполнения задачи
    """
    task_id = request.GET.get("task_id")
    return render(request, "pages/logs.html", {"task_id": task_id})


def logs_data_view(request: HttpRequest) -> JsonResponse:
    """
    Получение логов выполнения задачи
    """
    # return JsonResponse({"logs": TASK_LOGS, "running": TASK_RUNNING})
    task_id = request.GET.get("task_id")
    cache_key = f"task_logs_{task_id}"

    logs = cache.get(cache_key, [])
    return JsonResponse({"logs": logs})
