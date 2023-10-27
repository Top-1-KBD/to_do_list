FROM python:3.8

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY setup.py /app/setup.py
COPY README.md /app/README.md
COPY pyproject.toml /app/pyproject.toml
# COPY PyPI-Recovery-Codes-ErwanR92-2023-10-19T14 00 20.135638.txt /app/PyPI-Recovery-Codes-ErwanR92-2023-10-19T14 00 20.135638.txt
COPY poetry.lock /app/poetry.lock
COPY todolist /app/todolist
COPY docs /app/docs
# Commande à exécuter lorsque le conteneur démarre
CMD ["python", "task.py"]
