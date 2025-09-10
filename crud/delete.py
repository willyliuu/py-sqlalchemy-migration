from models import Place

def delete_place(session, name):
    place = session.query(Place).filter_by(name=name).first()
    if place:
        session.delete(place)
        session.commit()
        return True
    return False
