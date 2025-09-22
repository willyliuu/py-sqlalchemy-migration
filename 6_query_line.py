from shapely.geometry import box
from geoalchemy2.shape import from_shape, to_shape
from sqlalchemy import func
from models import SpatialFeature
from db import SessionLocal

def find_lines_in_bbox(bbox):
    try:
        session = SessionLocal()
        lines = (
            session.query(SpatialFeature)
            .filter(func.ST_Intersects(SpatialFeature.line, bbox))
            .all()
        )
        return lines
    except Exception as e:
        print(f"Error occurred: {e}")
        return []
    finally:
        session.close()

# Example usage
if __name__ == "__main__":
    # Define a bounding box (minx, miny, maxx, maxy)
    bbox_shape = box(106.8, -6.2, 107.0, -6.0)  # Example bbox around Jakarta
    bbox = from_shape(bbox_shape, srid=4326)

    lines_in_bbox = find_lines_in_bbox(bbox)
    for line in lines_in_bbox:
        print(f"Found line: {line.name} with geometry {to_shape(line.line)}")


def interpolate_point_along_line():
    try:
        session = SessionLocal()
        result = session.query(SpatialFeature.name, func.ST_AsText(func.ST_LineInterpolatePoint(SpatialFeature.line, 0.25)).label("point")).all()
        return result
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
    finally:
        session.close()

# Example usage
if __name__ == "__main__":
    points = interpolate_point_along_line()
    for name, point in points:
        print(f"Line: {name}, Interpolated Point at 25%: {point}")