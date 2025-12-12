from time import sleep

from django.core.cache import cache
from django.test import TestCase

from pages.tasks import long_process_task

# class CeleryTaskExecutionTest(TestCase):
#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()

#         # ⚠️ Замени project_name на имя своего Django проекта (где celery.py)
#         cls.worker = subprocess.Popen(
#             ["celery", "-A", "testaskdjango", "worker", "--loglevel=INFO"],
#         )

#         # Даем worker время подняться
#         time.sleep(2)

#     @classmethod
#     def tearDownClass(cls):
#         cls.worker.terminate()
#         cls.worker.wait()
#         super().tearDownClass()

#     def test_task_starts_and_finishes(self):
#         """
#         Тест подтверждает:
#         - задача НАЧАЛАСЬ (есть лог "Running for 1 seconds...")
#         - задача ЗАВЕРШИЛАСЬ (есть лог "Задача завершена")
#         """

#         # Запускаем задачу нормально через Celery
#         async_res = long_process_task.delay(1)

#         # Ждём завершения выполнения workerом
#         result = async_res.get(timeout=10)

#         # Проверяем успешность
#         self.assertTrue(result)
#         self.assertEqual(async_res.status, "SUCCESS")

#         # Достаём логи из кэша
#         cache_key = f"task_logs_{async_res.id}"
#         logs = cache.get(cache_key)
#         print("sdf")

#         # Подтверждаем, что задача НАЧАЛАСЬ
#         self.assertIsNotNone(logs, "Логи задач отсутствуют — задача не стартовала")
#         self.assertIn("Running for 1 seconds...", logs, "В кэше нет логов выполнения — задача не запускалась")

#         # Подтверждаем, что задача ЗАВЕРШИЛАСЬ
#         self.assertIn("Задача завершена ✅", logs, "Нет финального лога — задача не завершилась")


class CeleryTestCase(TestCase):
    fixtures = []

    def test_long_process_task(self):
        seconds = 5
        task = long_process_task.delay(seconds)
        cache_key = f"task_logs_{task.id}"

        sleep(2)
        logs = cache.get(cache_key, [])
        self.assertTrue(len(logs) > 0)
        self.assertEqual(logs[0], "Running for 1 seconds...")
        # TODO: check status of a task if possible
        # self.assertEqual(task.status, "running")

        sleep(5)
        logs = cache.get(cache_key, [])
        self.assertEqual(len(logs), seconds + 1)

        # TODO: check status of a task if possible
        # self.assertEqual(task.status, "success")

        sleep(2)
        logs = cache.get(cache_key, [])
        self.assertEqual(len(logs), seconds + 1)
