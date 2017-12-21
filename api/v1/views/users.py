#!/usr/bin/python3
"""new view for User objects"""
from flask import jsonify, request, abort
from api.v1.views import app_views
from models.user import User
from models import storage


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def all_users():
    """Retrieves the list of all user objects"""
    user = storage.get("User", user_id)
    list_users = []
    users_all = storage.all("User")

    if user is None:
        abort(404)
    for item in users_all.values():
        list_users.append(item.to_dict())
    return jsonify(list_users)


@app_views.route('/users/user_id', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """Retrieves the State object"""
    user = storage.get("User", user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """Deletes an object"""
    user = storage.get("User", user_id)
    if user is None:
        abort(404)
    user.delete()
    storage.save()
    storage.close()
    return jsonify({}), 200


@app_views.route('/states/<state_id>/users', methods=['POST'],
                 strict_slashes=False)
def create_user(s):
    """Creates a User"""
    body_dict = request.get_json
    if not request.is_json:
        abort(404, "Not a JSON")
    email = body_dict.get('email')
    if not password:
        abort(400, "Missing password")
    new_user = User(**body_dict)
    storage.new(new_user)
    new_user.save()
    storage.close()
    return jsonify(new_user.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """Updates a user object"""
    user = storage.get("User", user_id)
    if user is None:
        abort(404)

    body_dict = request.get_json()
    if not request.is_json:
        abort(404, "Not a JSON")

    ignore_keys = ["id", "state_id", "created_at", "updated_at"]
    for key, value in dict_body.items():
        if key not in ignore_keys:
            setattr(user, key, value)
    user.save()
    storage.close()
    return jsonify(user.to_dict()), 200