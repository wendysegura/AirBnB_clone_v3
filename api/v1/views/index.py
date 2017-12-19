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

@app_views.route('/api/v1/stats')
def get_count():
    """"retrieves the number of each objects by type"""
    count = {}
    
    name2class = {
    'Amenity': Amenity,
    'City': City,
    'Place': Place,
    'State': State,
    'Review': Review,
    'User': User
}
    for cls in name2class:
        number = storage.count(cls)
        count[name2class.get(cls)] = number
    return jsonify(count)
