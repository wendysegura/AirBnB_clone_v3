#!/usr/bin/python3
"""creates a new view for Amenity objects"""
from models import storagey
from api.v1.views import app_views
from flask import Flask, abort, request, jsonify
from models.city import City
from models.state import State


@app_views.route('/amenities', methods=['GET'],
                 strict_slashes=False)
def get_amenities():
    """ retrieves the list of all amenities obj """
    all_amenities = []
    amenities = storage.all('Amenities').values()
    for a in amenities:
        all_amenities.append(a.to_dict())
    return jsonify(all_amenities)


@app_views.route('/amenities/<amenity_id>', methods=['GET'],
                 strict_slashes=False)
def get_id(amenity_id):
    """ retrieves State object """
    amenity = storage.get("Amenity", amenity_id)
    if amenity is None:
        abort(404)
    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_amenity(amenity_id):
    """ delete State object if no id """
    amenity = storage.get("Amenity", amenity_id)
    empty = {}
    if amenity is None:
        abort(404)
    storage.delete(amenity)
    storage.save()
    storage.close()
    return (jsonify(empty), 200)


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def create_amenity(amenity_id):
    """ creates State object """
    req = request.get_json()
    if not request.is_json:
        abort(("Not a JSON"), 400)
    if not "name":
        abort(("Missing name"), 400)
    amenity = Amenity(**req)
    amenity.save()
    storage.close()
    return (jsonify(amenity.to_dict()), 201)


@app_views.route('/amenities/<amenity_id>', methods=['PUT'],
                 strict_slashes=False)
def update_amenity(amenity_id):
    amenity = storage.get("Amenity", amenity_id)
    if state is None:
        abort(404)
    req = request.get_json
    if not req:
        abort(404, "Not a JSON")
    ignore_keys = ["id", "created_at", "updated_at"]

    for key, value in req.items():
        if key not in ignore_keys:
            setattr(self, key, value)
    amenity.save()
    storage.close()
    return jsonify(amenity.to_dict()), 200
