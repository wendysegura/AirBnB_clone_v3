#!/usr/bin/python3
"""creates a new view for State objects"""
from models import storage
from models.state import State
from api.v1.views import app_views
from flask import Flask, abort, request, jsonify, Blueprint
from models.city import City

states = Blueprint("states", __name__)


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_state():
    """ retrieves the list of all State obj """
    all_state = []
    states = storage.all('State').values()
    for s in states:
        all_state.append(s.to_dict())
    return jsonify(all_state)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_id(state_id):
    """ retrieves State object """
    state = storage.get("State", state_id)
    return jsonify(state.to_dict())
    abort(404)


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id):
    """ delete State object if no id """
    state = storage.get("State", state_id)
    empty = {}
    if state == state.id:
        storage.delete(state)
        storage.save()
        return (jsonify(empty), 200)
    abort(404)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """ creates State object """
    req = request.get_json()
    if req is None:
        abort("Not a JSON", 400)
    if "name" not in req:
        abort("Missing name", 400)
    state = State(**req)
    storage.new(state)
    storage.save()
    return jsonify(state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """update"""
    state = storage.get("State", state_id)
    req = request.get_json
    if not req:
        abort(400, "Not a JSON")
    ignore_keys = ["id", "created_at", "updated_at"]
    if state:
        for key, value in req.items():
            if key not in ignore_keys:
                setattr(self, key, value)
        storage.save()
        return jsonify(state.to_dict())
    abort(404)
