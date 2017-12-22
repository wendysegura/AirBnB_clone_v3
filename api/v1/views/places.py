#!/usr/bin/python3
"""new view for Place objects"""
from flask import jsonify, request, abort
from api.v1.views import app_views
from models.place import Place
from models.city import City
from models import storage


@app_views.route('/cities/<city_id>/places', methods=['GET'],
                 strict_slashes=False)
def all_places(city_id):
    """Retrieves the list of all place objects"""
    city = storage.get("City", city_id)
    list_places = []
    places = storage.all("Place")

    if city is None:
        abort(404)
    for item in places.values():
        if item.city_id == city_id:
            list_places.append(item.to_dict())
    return jsonify(list_places)


@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
def get_place(place_id):
    """Retrieves the State object"""
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)
    return jsonify(place.to_dict())


@app_views.route('/places/<place_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_place(place_id):
    """Deletes an object"""
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)
    place.delete()
    storage.save()
    storage.close()
    return jsonify({}), 200


@app_views.route('/cities/<city_id>/places', methods=['POST'],
                 strict_slashes=False)
def create_place(city_id):
    """Creates a Place"""
    city = storage.get("City", city_id)
    if city is None:
        abort(404)
    body_dict = request.get_json()
    if not request.is_json:
        abort(400, "Not a JSON")
    user_id = body_dict.get("user_id")
    if not user_id:
        abort(400, "Missing user_id")
    user = storage.get("User", user_id)
    if user is None:
        abort(404)
    name = body_dict.get('name')
    if not name:
        abort(400, "Missing name")
    new_place = Place(**body_dict)
    storage.new(new_place)
    new_place.save()
    storage.close()
    return jsonify(new_place.to_dict()), 201


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def update_place(place_id):
    """Updates a place object"""
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)

    body_dict = request.get_json()
    if not request.is_json:
        abort(400, "Not a JSON")

    ignore_keys = ["id", "user_id", "city_id", "created_at", "updated_at"]
    for key, value in body_dict.items():
        if key not in ignore_keys:
            setattr(place, key, value)
    place.save()
    storage.close()
    return jsonify(place.to_dict()), 200
