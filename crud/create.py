from models import Place

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


