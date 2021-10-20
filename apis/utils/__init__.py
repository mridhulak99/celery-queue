from apis.utils.database_manager import DatabaseManager

database = DatabaseManager()
db = database.db

def init_app(app):
    database.init_app(app)