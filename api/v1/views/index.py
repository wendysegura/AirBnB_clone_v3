#!/usr/bin/python3
"""routing"""
from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage


@app_views.route('/status')
def response_status():
    """return json on object appviews"""
    response = jsonify({'status':'OK'})
    return response

@app_views.route('/stats')
def get_count():
    """"retrieves the number of each objects by type"""
    obj= {}
    name2class = {
    "amenities": "Amenity",
    "cities": "City",
    "places": "Place",
    "reviews": "Review",
    "states": "State",
    "users": "User"
}
    for cls in name2class:
        number = storage.count(obj)
        obj[name2class.get(cls)] = number
    return jsonify(obj)
