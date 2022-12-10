FROM python:3.9.15-slim

EXPOSE 5672

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN python producer 1 &
CMD [ "python", "producer", "2" ]
