#!/usr/bin/python3
"""API"""

from os import getenv
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from flask import jsonify


app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def close(self):
    storage.close()

<<<<<<< HEAD
@app.errorhandler(404)
def page_not_found(error):
    return jsonify(error='Not found'), 404
=======

@app.errorhandler(404)
def page_not_found(error):
return jsonify(error='Not found'), 404
>>>>>>> 13ef354b8f0bd5f3c3d5dd8a81e6786df316cfba

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
