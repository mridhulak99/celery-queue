FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=app
ENV FLASK_ENVIRONMENT=development
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers build-base bash libressl-dev musl-dev libffi-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .

CMD python run_flask_app.py


#RUN ["celery", "-A", "celery_task.celery_task", "worker"]