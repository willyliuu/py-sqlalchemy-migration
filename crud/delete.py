from models import Place

def delete_place(session, name):
    try:
        place = session.query(Place).filter_by(name=name).first()
        if place:
            session.delete(place)
            session.commit()
        return True
    except Exception as e:
        print(f"Error occurred: {e}")
        session.rollback()
        return False
    finally:
        session.close()
