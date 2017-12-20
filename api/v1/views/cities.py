#!/usr/bin/python3
"""new view for City objects"""


from flask import jsonify, request, abort
from api.v1.views import app_views
from models.city import City
from models import storage


@app_views.route('/states/<state_id>/cities', methods=['GET'], strict_slashes=False)
def all_cities(state_id):
    """Retrieves the list of all city objects"""
    state = storage.get("State", state_id)
    list_cities = []

    if not state:
        abort(404)
    for city in state.cities:
        if city.state_id == state_id:
            list_cities.append(city.to_dict())
    return jsonify(list_cities)
    
@app_views.route('/cities/city_id', methods=['GET'])
def get_city(city_id):
    """Retrieves the State object"""
    city = storage.get("City", city_id)
    if not city:
        abort(404)
    return jsonify(city.to_dict())

@app_views.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    """Deletes an object"""
    city = storage.get("City", city_id)
    if not city:
        abort(404)
    storage.delete(city)
    storage.save()
    return jsonify({}), 200

@app_views.route('/states/<state_id>/cities', methods=['POST'], strict_slashes=False)
def create_city(state_id):
    """Creates a City"""
    state = storage.get("State", state_id)
    if not city:
        abort(404)
    

@app_views.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    """Updates a city object"""
    if not city:
        abort(404)
