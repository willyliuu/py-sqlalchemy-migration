from db import SessionLocal
from models import SpatialFeature
from geoalchemy2.shape import from_shape, to_shape
from shapely.geometry import Point, LineString, Polygon

# ---- CRUD EXAMPLES ----
def create_feature():
    try:
      session = SessionLocal()

      point_geom = from_shape(Point(106.82, -6.17), srid=4326)   # Jakarta
      line_geom = from_shape(LineString([(106.82, -6.17), (107.0, -6.2)]), srid=4326)
      polygon_geom = from_shape(Polygon([
          (106.80, -6.18), (106.85, -6.18),
          (106.85, -6.15), (106.80, -6.15),
          (106.80, -6.18)
      ]), srid=4326)

      feature = SpatialFeature(
          name="Example Feature",
          point=point_geom,
          line=line_geom,
          polygon=polygon_geom
      )

      session.add(feature)
      session.commit()
      session.refresh(feature)

      print(f"Created feature with ID {feature.id}")
      return feature.id
    except Exception as e:
        print(f"Error occurred: {e}")
        session.rollback()
        return None
    finally:
        session.close()


def read_features():
  try:
    session = SessionLocal()
    features = session.query(SpatialFeature).all()
    return features
  except Exception as e:
    print(f"Error occurred: {e}")
    return []
  finally:
    session.close()


def update_feature(feature_id, new_name):
    try:
        session = SessionLocal()
        feature = session.query(SpatialFeature).filter(SpatialFeature.id == feature_id).first()
        if feature:
            feature.name = new_name
            session.commit()
            print(f"Updated feature {feature_id} name to {new_name}")
        else:
            print("Feature not found")
    except Exception as e:
        print(f"Error occurred: {e}")
        session.rollback()
    finally:
        session.close()


def delete_feature(feature_id):
    try:
        session = SessionLocal()
        feature = session.query(SpatialFeature).filter(SpatialFeature.id == feature_id).first()
        if feature:
            session.delete(feature)
            session.commit()
            print(f"Deleted feature {feature_id}")
        else:
            print("Feature not found")
    except Exception as e:
        print(f"Error occurred: {e}")
        session.rollback()
    finally:
        session.close()

# ---- Run Example ----
if __name__ == "__main__":
    feature_id = create_feature()
    read_features()
    update_feature(feature_id, "Updated Feature")
    read_features()
    delete_feature(feature_id)
    read_features()