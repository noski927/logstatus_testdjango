import time

from celery import shared_task
from django.core.cache import cache


@shared_task(bind=True)
def long_process_task(self, num_seconds: int):
    """
    Celery-фоновая задача
    """
    cache_key = f"task_logs_{self.request.id}"
    logs = []

    for i in range(num_seconds):
        msg = f"Running for {i + 1} seconds..."
        logs.append(msg)
        cache.set(cache_key, logs, timeout=3600)
        time.sleep(1)

    logs.append("Задача завершена ✅")
    cache.set(cache_key, logs, timeout=3600)

    return True