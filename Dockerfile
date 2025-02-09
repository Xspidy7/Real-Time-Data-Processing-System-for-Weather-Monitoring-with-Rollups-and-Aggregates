
FROM python:3.9-slim

WORKDIR /app

COPY ./src /app/src
COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

CMD ["python", "src/main.py"]
