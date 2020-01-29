from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_security

Base = declarative_base()

class User(Base):
	__tablename__ = 'users'

	user_id = Column(Integer, primary_key=True)

	name = Column(String)
	password = Column(String)

class Canvas(Base):
	__tablename__ = 'canvases'

	canvas_id = Column(Integer, primary_key=True)
	name = Column(String)
	user_id = Column(Integer)


class CanvasHistory(Base):
	__tablename__ = 'history'
	canvas_history_id = Column(Integer, primary_key=True)
	canvas_id = Column(Integer)
	history_point = Column(Integer)
	data = Column(String)