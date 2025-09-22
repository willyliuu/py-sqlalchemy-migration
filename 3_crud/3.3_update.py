from models import Place, User

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

def update_user_status(session, user_id, is_active):
    try:
        user = session.query(User).filter_by(id=user_id).first()
        if user:
            user.is_active = is_active
            session.commit()
            return user
    except Exception as e:
        print(f"Error occurred: {e}")
        session.rollback()
    finally:
        session.close()
    return None