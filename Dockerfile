FROM python:3.8.5

WORKDIR /app

COPY requirements.txt .

#RUN apt-get update && apt-get install -y python3-pip
RUN pip install -r requirements.txt

COPY setup.py /app/setup.py
COPY README.md /app/README.md
COPY pyproject.toml /app/pyproject.toml
# COPY PyPI-Recovery-Codes-ErwanR92-2023-10-19T14 00 20.135638.txt /app/PyPI-Recovery-Codes-ErwanR92-2023-10-19T14 00 20.135638.txt
COPY poetry.lock /app/poetry.lock
COPY tests /app/tests
COPY logger /app/logger
COPY models /app/models
COPY exceptions /app/exceptions
COPY docs /app/docs
COPY logs /app/logs
COPY bin /app/bin
COPY app.py /app/app.py
COPY To_do_list.db /app/To_do_list.db
# Commande à exécuter lorsque le conteneur démarre
CMD ["python3"]
