import threading
import time

from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect, render

TASK_LOGS = []
TASK_RUNNING = False


def long_process(num_seconds: int) -> None:
    """
    Функция имитирующая длительную задачу
    """
    global TASK_LOGS, TASK_RUNNING
    TASK_LOGS = []
    TASK_RUNNING = True
    for i in range(num_seconds):  # имитация длительной задачи
        msg = f"Running for {i + 1} seconds..."
        print(msg)
        TASK_LOGS.append(msg)  # сохраняем в память для фронта
        time.sleep(1)  # интервал в работе
    TASK_LOGS.append("Задача завершена ✅")
    TASK_RUNNING = False


def index(request: HttpRequest) -> render:
    """
    Отображает основную страницу приложения с формой
    """
    status = request.GET.get("status")
    return render(request, "pages/index.html", {"status": status})


def start_task(request: HttpRequest) -> redirect:
    """
    Запуск длительной задачи в отдельном потоке
    """
    if request.method == "POST":
        seconds = int(request.POST.get("seconds", 5))
        thread = threading.Thread(target=long_process, args=(seconds,))
        thread.start()
        return redirect("logs")
    return redirect("index")


def logs_view(request: HttpRequest) -> render:
    """
    Отображение логов выполнения задачи
    """
    return render(request, "pages/logs.html")


def get_logs(request: HttpRequest) -> JsonResponse:
    """
    Получение логов выполнения задачи
    """
    return JsonResponse({"logs": TASK_LOGS, "running": TASK_RUNNING})
