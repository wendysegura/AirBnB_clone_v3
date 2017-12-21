#!/usr/bin/python3
"""new view for Review  objects"""
from flask import jsonify, request, abort
from api.v1.views import app_views
from models.place import Place
from models.city import City
from models import storage


@app_views.route('/places/<place_id>/reviews', methods=['GET'],
                 strict_slashes=False)
def all_places(place_id):
    """Retrieves the list of all review objects"""
    place = storage.get("Place", place_id)
    list_reviews = []
    all_reviews = storage.all("Review")

    if place is None:
        abort(404)
    for item in all_reviews.values():
        if item.place_id == place_id:
            list_reviews.append(item.to_dict())
    return jsonify(list_reviews)


@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def get_review(review_id):
    """Retrieves the review object"""
    review = storage.get("Review", review_id)
    if review is None:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route('/reviews/<review_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_review(review_id):
    """Deletes an object"""
    review = storage.get("Review", review_id)
    if review is None:
        abort(404)
    review.delete()
    storage.save()
    storage.close()
    return jsonify({}), 200


@app_views.route('/places/<place_id>/reviews', methods=['POST'],
                 strict_slashes=False)
def create_review(place_id):
    """Creates a Review"""
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)
    body_dict = request.get_json
    if not request.is_json:
        abort(400, "Not a JSON")
    user_id = body_dict.get("user_id")
    if not user_id:
        abort(400, "Missing user_id")
    if user_id is None:
        abort(404)
    text = body_dict.get('text')
    if not text:
        abort(400, "Missing text")
    new_review = Review(**body_dict)
    new_rewview.place_id = place_id
    storage.new(new_review)
    new_review.save()
    storage.close()
    return jsonify(new_review.to_dict()), 201


@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def update_review(review_id):
    """Updates a review object"""
    review = storage.get("Review", review_id)
    if review is None:
        abort(404)

    body_dict = request.get_json()
    if not request.is_json:
        abort(404, "Not a JSON")

    ignore_keys = ["id", "user_id", "state_id", "created_at", "updated_at"]
    for key, value in dict_body.items():
        if key not in ignore_keys:
            setattr(review, key, value)
    review.save()
    storage.close()
    return jsonify(review.to_dict()), 200
