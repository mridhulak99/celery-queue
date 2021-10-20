# requirements.txt
pip install -r requirements.txt

# Flask application on port 5000
cd apis
set FLASK_APP=app
flask run ==host=0.0.0.0 --port=5000

# Celery task for handling messaging broker- rabbit mq
celery -A celery_task.celery_task worker

# Swagger File
http://localhost:5000/ui
