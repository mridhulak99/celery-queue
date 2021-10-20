from flask_sqlalchemy import SQLAlchemy

class DatabaseManager:
    def __init__(self):
        self.db = SQLAlchemy()
    
    def init_app(self, app):
        import apis.models as models
        models.load()
        self.db.init_app(app)
        self.db.create_all(app=app)
    
    def check_connextion(self):
        try:
            with self.db.engine.connect() as connection:
                connection.execute("select 1;")
            return True
        except Exception:
            return False
