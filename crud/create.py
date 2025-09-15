from models import Place, User

def create_place(session, name, lon, lat):
    try:
        wkt_point = f"SRID=4326;POINT({lon} {lat})"
        new_place = Place(name=name, location=wkt_point)
        session.add(new_place)
        session.commit()
        session.refresh(new_place)
        return new_place
    except Exception as e:
        print(f"Error occurred: {e}")
        session.rollback()
    finally:
        session.close()

def create_user(session, name, is_active=True):
    try:
        new_user = User(name=name, is_active=is_active)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user
    except Exception as e:
        print(f"Error occurred: {e}")
        session.rollback()
    finally:
        session.close()


