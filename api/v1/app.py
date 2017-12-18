#!/usr/bin/python3
"""API"""
app = Flask('app_views')
from models import storage
from api.v1.views import app_views

@app.teardown_appcontext
def close():
    return storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
