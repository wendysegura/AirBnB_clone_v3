#!/usr/bin/python3
"""API"""
app = Flask('app_views')
from models import storage
from api.v1.views import app_views
from flask import jsonify

@app.teardown_appcontext
def close():
    return storage.close()

@app.errorhandler(404)
def page_not_found(error):
    return jsonify(error='Not found'), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
