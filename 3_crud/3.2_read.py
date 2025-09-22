from models import Place, User

def get_places(session):
    return session.query(Place).all()

def get_place_by_name(session, name):
    return session.query(Place).filter_by(name=name).first()

def get_users(session):
    return session.query(User).all()

def get_user_by_id(session, user_id):
    return session.query(User).filter_by(id=user_id).first()
