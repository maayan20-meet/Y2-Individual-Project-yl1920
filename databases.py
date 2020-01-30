from model import Base, User, Canvas, CanvasHistory
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# engine = create_engine('sqlite:///database.db')
# Base.metadata.create_all(engine)
# DBSession = sessionmaker(bind=engine)
# session = DBSession()


def create_thread():
	engine = create_engine('sqlite:///database.db')
	Base.metadata.create_all(engine)
	DBSession = sessionmaker(bind=engine)
	session = DBSession()
	return session

def add_user(name, password):

	session = create_thread()
	user = User(name=name, password=password)

	session.add(user)
	session.commit()

def get_pass(name):

	session = create_thread()

	return session.query(User).filter_by(name=name).first().password

def user_exist(name):

	session = create_thread()

	user = session.query(User).filter_by(name=name).first()

	return user is not None

def get_user_id(name):

	session = create_thread()

	return session.query(User).filter_by(name=name).first().user_id

#Canvas functions:

def new_history_point(data, canvas_id):

	session = create_thread()

	lateset_point = get_lateset_point(canvas_id)

	history_point = 0

	if lateset_point is not None:
		history_point = lateset_point.history_point + 1

	point = CanvasHistory(canvas_id=canvas_id, history_point=history_point, data=data)

	session.add(point)
	session.commit()


def get_lateset_point(canvas_id):

	session = create_thread()

	points = session.query(CanvasHistory).filter_by(canvas_id=canvas_id).all()

	if not points:
		return None

	max_point = points[0]

	for point in points:

		if point.history_point > max_point.history_point:
			max_point = point

	return max_point

def get_canvas(canvas_id):

	session = create_thread()

	return session.query(Canvas).filter_by(canvas_id=canvas_id).first()

def get_all_canvases():

	session = create_thread()

	return session.query(Canvas).all()

def get_canvases_by_name(name):

	session = create_thread()

	return session.query(Canvas).filter_by(name=name).all()

def get_canvases_by_user_id(user_id):

	session = create_thread()

	return session.query(Canvas).filter_by(user_id=user_id).all()

def create_canvas(canvas_name, user_name):

	session = create_thread()

	canvas = Canvas(name=canvas_name, user_name=user_name, user_id=get_user_id(user_name))
	session.add(canvas)
	session.commit()

	return canvas

def get_canvas_name(canvas_id):

	session = create_thread()

	return session.query(Canvas).filter_by(canvas_id=canvas_id).first().name