from models import Place, User
from geoalchemy2.shape import from_shape
from shapely.geometry import Point

def create_place(session, name, lon, lat):
    try:
        geom = from_shape(Point(lon, lat), srid=4326)
        new_place = Place(name=name, location=geom)
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


