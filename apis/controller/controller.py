from apis.core.db_operations import (
    add_to_db,
    get_from_db
)


def hello_world():
    return "hi from api test", 200


def add_numbers(**kwargs):
    x = kwargs.get('x')
    y = kwargs.get('y')
    res = add_to_db(x, y)
    return res


def get_numbers(**kwargs):
    identifier = kwargs.get('identifier')
    res = get_from_db(identifier)
    if res:
        return res, 200
    else:
        return "Identifier does not exist", 404
