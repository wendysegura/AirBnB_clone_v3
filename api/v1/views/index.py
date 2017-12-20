#!/usr/bin/python3
"""routing"""
from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage
from models.state import State
from models.city import City
from models.base_model import BaseModel
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


@app_views.route('/status/', strict_slashes=False)
def response_status():
    """return json on object appviews"""
    response = jsonify({'status': 'OK'})
    return response


@app_views.route('/stats/', strict_slashes=False)
def get_count():
    """"retrieves the number of each objects by type"""
    obj = {}
    name2class = {"amenities": "Amenity",
                  "cities": "City",
                  "places": "Place",
                  "reviews": "Review",
                  "states": "State",
                  "users": "User"}

    for cls in name2class.keys():
        number = storage.count(obj)
        obj[name2class[cls]] = number
    return jsonify(obj)
