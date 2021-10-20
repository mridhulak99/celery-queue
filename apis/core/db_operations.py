from apis.utils import db
from apis.models.sum_ import Sum
from celery_task.celery_task import add_number


def add_to_db(x, y):
    """
    Inserts x and x into db
    Schedules a celery task using rabbitmq with countdown as 10 sec.
    """
    sum_obj = Sum(x=x, y=y)
    db.session.add(sum_obj)
    db.session.commit()
    res = sum_obj.as_dict()
    # Adds to rabbit mq with countdown 
    add_number.apply_async(kwargs={
        "id": res['id_'],
        "x": res["x"],
        "y": res["y"]
    }, countdown=10)
    return res['id_']


def get_from_db(identifier):
    """
    Gets answer from db
    """
    res = Sum.query.filter_by(id_=identifier).first()
    if res:
        res = res.as_dict()
        return res['answer'] if res['answer'] else "please wait"
