#!/usr/bin/python3
"""new view for City objects"""
from models import storage
from models.state import State
from models.city import City
from flask import Flask, abort, request, jsonify, Blueprint

cities = Blueprint("cities", __name__)


@cities.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def all_cities(state_id):
    """Retrieves the list of all city objects"""
    all_city = []
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    all_cities = storage.all("City").values()
    for c in cities:
        if c.state_id == state_id:
            all_city.append(c.to_dict())
    return jsonify(all_city)


@cities.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_city(city_id):
    """Retrieves the State object"""
    city = storage.get("City", city_id)
    if city is None:
        abort(404)
    return jsonify(city.to_dict())


@cities.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    """Deletes an object"""
    city = storage.get("City", city_id)
    empty = {}
    if city is None:
        abort(404)
    city.delete()
    storage.save()
    storage.close()
    return (jsonify(empty), 200)


@cities.route('/states/<state_id>/cities', methods=['POST'],
                 strict_slashes=False)
def create_city(state_id):
    """Creates a City"""
    req = request.get_json
    if not request.is_json:
        abort(404, "Not a JSON")
    name = req.get('name')
    if not name:
        abort(400, "Missing name")
    city = City(**req)
    storage.new(city)
    storage.save()
    storage.close()
    return (jsonify(city.to_dict()), 201)


@cities.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    """Updates a city object"""
    city = storage.get("City", city_id)
    if not request.is_json:
        abort(400, "Not a JSON")
    if city is None:
        abort(404)
    req = request.get_json()
    ignore_keys = ["id", "state_id", "created_at", "updated_at"]
    if city:
        for key, value in req.items():
            if key not in ignore_keys:
                setattr(self, key, value)
    storage.save()
    storage.close()
    return jsonify(city.to_dict()), 200
