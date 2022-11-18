FROM python:3.9.15-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5671

CMD [ "python", "src/" ]