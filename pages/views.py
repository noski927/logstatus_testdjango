import time

from django.shortcuts import redirect, render

TASK_LOGS = []
TASK_RUNNING = False


def long_process(num_seconds: int):
    global TASK_LOGS, TASK_RUNNING
    TASK_LOGS = []
    TASK_RUNNING = True
    for i in range(num_seconds):
        msg = f"Running for {i + 1} seconds..."
        print(msg)  # видно в консоли
        TASK_LOGS.append(msg)  # сохраняем в память для фронта
        time.sleep(1)
    TASK_LOGS.append("Задача завершена ✅")
    TASK_RUNNING = False


def index(request):
    status = request.GET.get("status")
    return render(request, "pages/index.html", {"status": status})


def start_task(request):
    if request.method == "POST":
        seconds = int(request.POST.get("seconds", 5))
        thread = threading.Thread(target=long_process, args=(seconds,))
        thread.start()
        return redirect("logs")
    return redirect("index")


def logs_view(request):
    return render(request, "pages/logs.html")


def get_logs(request):
    return JsonResponse({"logs": TASK_LOGS, "running": TASK_RUNNING})
