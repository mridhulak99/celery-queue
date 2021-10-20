import os

APP_NAME = os.environ.get("APP_NAME", "local")
APP_ENVIRONMENT = os.environ.get("APP_ENVIRONMENT", "local")
SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", "sqlite:////home/mridhula/Documents/flask/flask-connexion/a.db")
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS", False)
RABBIT_MQ = os.environ.get("RABBIT_MQ", "amqp://guest:guest@localhost:5672/")
