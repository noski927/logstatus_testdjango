FROM continuumio/miniconda3:latest
WORKDIR /app

# Копируем conda-окружение
COPY env.yml /app/

# Создаем окружение
RUN conda env create -f env.yml

# Настраиваем shell для всех следующих команд (ключевой момент!)
SHELL ["conda", "run", "-n", "testdjango", "/bin/bash", "-c"]

# Копируем проект
COPY . /app/

# Чтобы внутри контейнера сразу был доступ к окружению
ENV PATH="/opt/conda/envs/testdjango/bin:$PATH"

# Запускаем Django через conda
CMD ["bash", "-c", "conda run -n testdjango python manage.py runserver 0.0.0.0:8000"]