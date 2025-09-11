from models import Place

def update_place_name(session, old_name, new_name):
    try:
        place = session.query(Place).filter_by(name=old_name).first()
        if place:
            place.name = new_name
            session.commit()
            return place
    except Exception as e:
        print(f"Error occurred: {e}")
        session.rollback()
    finally:
        session.close()
    return None
