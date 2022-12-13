FROM python:3.9.15-slim

EXPOSE 80

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD [ "flask", "--app", "main.py", "run", "--port=80", "--host=0.0.0.0" ]