
import os
import sys
sys.path.append(os.getcwd())
from celery_task.database import Sum, get_session
from celery import Celery
RABBIT_MQ = os.environ.get("RABBIT_MQ", "amqp://guest:guest@localhost:5672/")
# Celery task with tabbitmq as broker
app = Celery('tasks', broker=RABBIT_MQ)



@app.task(bind=True)
def add_number(self, id, x, y):
    """
    Adds numbers x and y and inserts into database filtered on id
    """

    ans = x + y
    session = get_session()
    res = session.query(Sum).filter(Sum.id_==id).first()
    res.answer = ans
    session.commit()
