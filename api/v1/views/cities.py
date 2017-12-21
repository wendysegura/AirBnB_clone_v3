#!/usr/bin/python3
"""new view for City objects"""
from flask import jsonify, request, abort
from api.v1.views import app_views
from models.city import City
from models import storage
from models.state import State
<<<<<<< HEAD
from models.city import City
from flask import Flask, abort, request, jsonify, Blueprint
=======
>>>>>>> parent of 1ee918f... made like state

cities = Blueprint("cities", __name__)

<<<<<<< HEAD

@cities.route('/states/<state_id>/cities', methods=['GET'],
              strict_slashes=False)
=======
@app_views.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
>>>>>>> parent of 1ee918f... made like state
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


<<<<<<< HEAD
@cities.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
=======
@app_views.route('/cities/city_id', methods=['GET'])
>>>>>>> parent of 1ee918f... made like state
def get_city(city_id):
    """Retrieves the State object"""
    city = storage.get("City", city_id)
    if city is None:
        abort(404)
    return jsonify(city.to_dict())


<<<<<<< HEAD
@cities.route('/cities/<city_id>', methods=['DELETE'])
=======
@app_views.route('/cities/<city_id>', methods=['DELETE'])
>>>>>>> parent of 1ee918f... made like state
def delete_city(city_id):
    """Deletes an object"""
    city = storage.get("City", city_id)
    if city is None:
        abort(404)
    city.delete()
    storage.save()
    storage.close()
    return jsonify({}), 200


@cities.route('/states/<state_id>/cities', methods=['POST'],
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
    city = City(**body_dict)
    storage.new(city)
    storage.save()
    storage.close()
    return jsonify(city_to_dict()), 201


<<<<<<< HEAD
@cities.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
=======
@app_views.route('/cities/<city_id>', methods=['PUT'])
>>>>>>> parent of 1ee918f... made like state
def update_city(city_id):
    """Updates a city object"""
    city = storage.get("City", city_id)
    if city is None:
        abort(404)

    body_dict = request.get_json()
    if not request.is_json:
        abort(404, "Not a JSON")

    ignore_keys = ["id", "state_id", "created_at", "updated_at"]
    for key, value in dict_body.items():
        if key not in ignore_keys:
            setattr(self, key, value)
    storage.save()
    storage.close()
    return jsonify(city.to_dict()), 200
