from shapely import LineString, Point
from geoalchemy2.shape import from_shape, to_shape
from sqlalchemy import func
from models import SpatialFeature
from db import SessionLocal

def test_point_inside_polygon():
    try:
        session = SessionLocal()
        point_shape = Point(106.81, -6.16)  # Example point in Jakarta
        point = from_shape(point_shape, srid=4326)
        points_inside = (
            session.query(SpatialFeature)
            .filter(func.ST_Contains(SpatialFeature.polygon, point))
            .all()
        )
        return points_inside
    except Exception as e:
        print(f"Error occurred: {e}")
        return []
    finally:
        session.close()

# Example usage
if __name__ == "__main__":
    points = test_point_inside_polygon()
    for point in points:
        print(f"Found point: {point.name} at {to_shape(point.point)}")

def find_polygons_intersecting_given_line():
    try:
        session = SessionLocal()
        line_shape = LineString([(106.79, -6.19), (106.86, -6.14)])  # Example line
        line = from_shape(line_shape, srid=4326)
        intersecting_polygons = (
            session.query(SpatialFeature)
            .filter(func.ST_Intersects(SpatialFeature.polygon, line))
            .all()
        )
        return intersecting_polygons
    except Exception as e:
        print(f"Error occurred: {e}")
        return []
    finally:
        session.close()

# Example usage
if __name__ == "__main__":
    polygons = find_polygons_intersecting_given_line()
    for polygon in polygons:
        print(f"Found polygon: {polygon.name} with geometry {to_shape(polygon.polygon)}")

def calculate_area_of_polygons():
    try:
        session = SessionLocal()
        areas = (
            session.query(SpatialFeature.name, func.ST_Area(SpatialFeature.polygon).label("area"))
            .all()
        )
        return areas
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
    finally:
        session.close()

# Example usage
if __name__ == "__main__":
    areas = calculate_area_of_polygons()
    for name, area in areas:
        print(f"Polygon: {name}, Area: {area} square meters")