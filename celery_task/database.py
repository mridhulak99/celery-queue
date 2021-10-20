from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
import os
SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", "sqlite:////home/mridhula/Documents/flask/flask-connexion/a.db")


engine = create_engine(SQLALCHEMY_DATABASE_URI, echo = True)
Base = declarative_base()

class Sum(Base):
   __tablename__ = 'sum_no'
   id_ = Column(Integer, primary_key=True , autoincrement=True)
   x = Column(Integer, nullable=True) 
   y = Column(Integer, nullable=True)
   answer = Column(Integer, nullable=True)

Base.metadata.create_all(engine)

def get_session():
   Session = sessionmaker(bind = engine)
   session = Session()
   return session