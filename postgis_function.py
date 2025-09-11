from geoalchemy2.shape import from_shape, to_shape
from shapely import Point
from sqlalchemy import func
from db import SessionLocal
from models import SpatialFeature


# Buffering a point and returning all polygons that intersect the buffer
def find_polygons_intersecting_buffered_point(point, buffer_distance):
    try:
        session = SessionLocal()
        buffered_point = point.buffer(buffer_distance)
        intersecting_polygons = (
            session.query(SpatialFeature)
            .filter(func.ST_Intersects(SpatialFeature.polygon, from_shape(buffered_point, srid=4326)))
            .all()
        )
        return intersecting_polygons
    except Exception as e:
        print(f"Error occurred: {e}")
        return []
    finally:
        session.close()

# Example usage:
if __name__ == "__main__":
    point = Point(106.81, -6.16)  # Example point in Jakarta
    buffer_distance = 100  # Buffer distance in meters
    polygons = find_polygons_intersecting_buffered_point(point, buffer_distance)
    for polygon in polygons:
        print(f"Found polygon: {polygon.name} with geometry {to_shape(polygon.polygon)}")
