#!/usr/bin/python3
"""new view for State objects"""


from flask import jsonify, 
from api.v1.views import app_views
from models.state import State
from models import storage


@app_views.route('/states',     )
def all_states():
    """Retrieves the list of all State objects"""
    """GET /api/v1/states"""



@app_views.route('/states',     )
def get_state():
    """Retrieves the State object"""
    """GET /api/v1/states/<state_id>"""


@app_views.route('/states',     )
def delete_state():
    """Deletes a State object"""
    """DELETE /api/v1/states/<state_id>"""


@app_views.route('/states',     )
def create_state():
    """Creates a State"""
    """POST /api/v1/states"""


@app_views.route('/states',     )
def update_state():
    """Updates a State object"""
    """PUT /api/v1/states/<state_id>"""
