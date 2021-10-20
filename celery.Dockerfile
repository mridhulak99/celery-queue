FROM python:3.7-alpine
WORKDIR /code
RUN apk add --no-cache gcc musl-dev linux-headers build-base bash libressl-dev musl-dev libffi-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD celery -A celery_task.celery_task worker
