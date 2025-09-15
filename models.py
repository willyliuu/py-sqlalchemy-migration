# models.py
from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from geoalchemy2 import Geometry
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    is_active = Column(Boolean, default=True)  # Boolean column
    created_at = Column(Date, default=datetime.date.today)  # Date column

class Place(Base):
    __tablename__ = "places"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    # Spatial column (POINT with SRID 4326 - GPS coordinates)
    location = Column(Geometry(geometry_type="POINT", srid=4326))

class SpatialFeature(Base):
    __tablename__ = "spatial_features"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    # Geometry columns
    point = Column(Geometry(geometry_type="POINT", srid=4326))
    line = Column(Geometry(geometry_type="LINESTRING", srid=4326))
    polygon = Column(Geometry(geometry_type="POLYGON", srid=4326))