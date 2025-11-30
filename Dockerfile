FROM continuumio/miniconda3:latest

WORKDIR /app

# Копируем env.yml
COPY env.yml .

# Создаём окружение conda
RUN conda env create -f env.yml

# Копируем проект
COPY . .

# CMD для Django с активацией окружения
CMD ["/bin/bash", "-c", "source /opt/conda/etc/profile.d/conda.sh && conda activate app_env && python manage.py runserver 0.0.0.0:8000"]
