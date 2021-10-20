from apis.utils import db

class Sum(db.Model):
    __tablename__ = 'sum_no'
    id_ = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    x = db.Column(db.Integer(), nullable=True)
    y = db.Column(db.Integer(), nullable=True)
    answer = db.Column(db.Integer(), nullable=True)

    def as_dict(self):
        return {
            "id_": self.id_,
            "x": self.x,
            "y": self.y,
            "answer": self.answer
        }
