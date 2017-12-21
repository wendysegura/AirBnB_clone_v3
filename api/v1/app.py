#!/usr/bin/python3
"""API"""
from os import getenv
from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify, Response
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})
app.register_blueprint(app_views)


@app.teardown_appcontext
def close(self):
    """teardown"""
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """error"""
    return jsonify(error='Not found'), 404

if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(getenv("HBNB_API_PORT", 5000))
    app.run(host=host, port=port)
