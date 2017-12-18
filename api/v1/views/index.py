from flask import Flask
from api.v1.views import app_views

@app.route('/status')
def response_status():
    """return json on object appviews"""
    response = JsonResponse({'status':'OK'})
    return response

@app.route('/api/v1/stats')
def get_count():
    """"retrieves the number of each objects by type"""
    
