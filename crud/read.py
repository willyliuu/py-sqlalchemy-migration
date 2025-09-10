from models import Place

def get_places(session):
    return session.query(Place).all()

def get_place_by_name(session, name):
    return session.query(Place).filter_by(name=name).first()
