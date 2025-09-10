from db import SessionLocal
from crud.create import create_place
from crud.read import get_places
from crud.update import update_place_name
from crud.delete import delete_place

session = SessionLocal()

# Create
p = create_place(session, "Central Park", -73.97, 40.77)
# print("Created:", p.id, p.name)

# # Read
places = get_places(session)
# print("Places:", [(pl.id, pl.name) for pl in places])

# # Update
updated = update_place_name(session, "Central Park", "NYC Central Park")
# print("Updated:", updated.name if updated else "Not found")

# # Delete
deleted = delete_place(session, "NYC Central Park")
# print("Deleted:", deleted)

session.close()