FROM continuumio/miniconda3:latest
WORKDIR /app
COPY env.yml /app/
RUN conda env create -f env.yml
SHELL ["conda", "run", "-n", "test-task-django", "/bin/bash", "-c"]
COPY . /app/
EXPOSE 8000
CMD ["conda", "run", "-n", "test-task-django", "python", "manage.py", "runserver", "0.0.0.0:8000"]
