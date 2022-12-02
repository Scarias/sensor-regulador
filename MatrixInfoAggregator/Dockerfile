FROM python:3.9.15-slim

EXPOSE 5672
EXPOSE 61613

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN python listener.py &
CMD [ "python", "sender.py" ]