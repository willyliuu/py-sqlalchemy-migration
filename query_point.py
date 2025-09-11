from shapely.geometry import Point
from geoalchemy2.shape import from_shape, to_shape
from sqlalchemy import func
from models import SpatialFeature
from db import SessionLocal


def find_nearby_places(lon, lat, distance_meters):
    try:
        session = SessionLocal()
        point = from_shape(Point(lon, lat), srid=4326)
        places = (
            session.query(SpatialFeature)
            .filter(func.ST_DWithin(SpatialFeature.point, point, distance_meters))
            .all()
        )
        return places
    except Exception as e:
        print(f"Error occurred: {e}")
        return []
    finally:
        session.close()

# Example usage
if __name__ == "__main__":
    lon, lat = -73.98, 40.76 # Example coordinates (New York City)
    distance = 5000   # 5 km
    nearby_places = find_nearby_places(lon, lat, distance)
    for place in nearby_places:
        print(f"Found place: {place.name} at {to_shape(place.point)}")


def place_with_distance(lon1, lat1):
    try:
        session = SessionLocal()
        point = from_shape(Point(lon1, lat1), srid=4326)
        places_with_distance = (
              session.query(SpatialFeature.name, func.ST_Distance(SpatialFeature.point, point).label("distance"))
              .all()
        )
        return places_with_distance
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
    finally:
        session.close()

# Example usage
if __name__ == "__main__":
    places = place_with_distance(-73.98, 40.76)
    for name, distance in places:
        print(f"Place: {name}, Distance: {distance} meters")
    