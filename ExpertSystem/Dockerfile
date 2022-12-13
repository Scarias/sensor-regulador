FROM python:3.9.15-slim

EXPOSE 80

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD [ "uwsgi", "--http", ":80", "--master", "-p", "4", "-w", "main:app" ]