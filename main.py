from db import SessionLocal
from crud.create import create_place, create_user
from crud.read import get_places, get_users, get_user_by_id
from crud.update import update_place_name, update_user_status
from crud.delete import delete_place, delete_user

session = SessionLocal()

# Create Usage
place = create_place(session, name="Central Park", lon=-73.965355, lat=40.782865)
print(place.id, place.name, place.location)

# Tambah user baru
user = create_user(session, name="Willy", is_active=True)
print(user.id, user.name, user.is_active)

# # Read
# places = get_places(session)
# print("Places:", [(pl.id, pl.name) for pl in places])

# Read users
users = get_users(session)
print("Users:", [(u.id, u.name) for u in users])

# Get user by ID
user = get_user_by_id(session, 1)
print("User with ID 1:", user.id, user.name, user.is_active)


# Update
# updated = update_place_name(session, "Central Park", "NYC Central Park")

# Update user
updated_user = update_user_status(session, 1, False)
print("Updated user:", updated_user.id, updated_user.name, updated_user.is_active)

# # Delete
# deleted = delete_place(session, "NYC Central Park")
# print("Deleted:", deleted)

# Delete user
deleted_user = delete_user(session, 1)
print("Deleted user:", deleted_user)

# session.close()