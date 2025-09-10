from models import Place

def update_place_name(session, old_name, new_name):
    place = session.query(Place).filter_by(name=old_name).first()
    if place:
        place.name = new_name
        session.commit()
        return place
    return None
