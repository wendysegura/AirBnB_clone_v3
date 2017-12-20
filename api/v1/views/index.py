#!/usr/bin/python3
"""routing"""
from api.v1.views import app_views, storage
from flask import Flask, jsonify
from models import storage
from models.state import State
from models.city import City


@app_views.route('/status', strict_slasher=False)
def response_status():
    """return json on object appviews"""
    response = jsonify({'status': 'OK'})
    return response


@app_views.route('/stats', strict_slashes=False)
def get_count():
    """"retrieves the number of each objects by type"""
    obj = {}
    name2class = {"amenities": "Amenity",
                  "cities": "City",
                  "places": "Place",
                  "reviews": "Review",
                  "states": "State",
                  "users": "User"}

    for cls in name2class:
        number = storage.count(obj)
        obj[name2class[cls]] = number
    return jsonify(obj)
