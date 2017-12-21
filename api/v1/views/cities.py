#!/usr/bin/python3
"""new view for City objects"""
from flask import jsonify, request, abort
from api.v1.views import app_views
from models.city import City
from models import storage
from models.state import State


@app_views.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def all_cities(state_id):
    """Retrieves the list of all city objects"""
    state = storage.get("State", state_id)
    list_cities = []
    all_cities = storage.all("City")

    if state is None:
        abort(404)
    for item in all_cities.values():
        if item.state_id == state_id:
            list_cities.append(item.to_dict())
    return jsonify(list_cities)


@app_views.route('/cities/city_id', methods=['GET'], strict_slashes=False)
def obj_city(city_id):
    """Retrieves the State object"""
    city = storage.get("City", city_id)
    if city is None:
        abort(404)
    return jsonify(city.to_dict())


@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def delete_city(city_id):
    """Deletes an object"""
    city = storage.get("City", city_id)
    if city is None:
        abort(404)
    city.delete()
    storage.save()
    storage.close()
    return jsonify({}), 200


@app_views.route('/states/<state_id>/cities', methods=['POST'],
                 strict_slashes=False)
def create_city(state_id):
    """Creates a City"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    body_dict = request.get_json
    if not request.is_json:
        abort(404, "Not a JSON")
    name = body_dict.get('name')
    if not name:
        abort(404, "Missing name")
    upd_city = City(**body_dict)
    storage.new(upd_city)
    storage.save()
    storage.close()
    return jsonify(upd_city.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    """Updates a city object"""
    body_dict = request.get_json()
    if not request.is_json:
        abort(404, "Not a JSON")
    city = storage.get("City", city_id)
    if city is None:
        abort(404)

    ignore_keys = ["id", "state_id", "created_at", "updated_at"]
    for key, value in dict_body.items():
        if key not in ignore_keys:
            setattr(self, key, value)
    storage.save()
    storage.close()
    return jsonify(city.to_dict()), 200
