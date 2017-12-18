from api.v1.views import app_views

@app.route('/status')
def response_status():
    """return json on object appviews"""
    response = JsonResponse({'status':'OK'})
    return response
