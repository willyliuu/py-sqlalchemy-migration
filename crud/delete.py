from models import Place, User

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

def delete_user(session, user_id):
    try:
        user = session.query(User).filter_by(id=user_id).first()
        if user:
            session.delete(user)
            session.commit()
        return True
    except Exception as e:
        print(f"Error occurred: {e}")
        session.rollback()
        return False
    finally:
        session.close()