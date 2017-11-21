from flask import Blueprint
from flask import request
from flask import current_app as app
import pymysql
import requests

controller = Blueprint('prediction', __name__, template_folder='templates')
 
accessKey = app.config.ACCESSKEY
@controller.route('/<count>', methods=['GET'])
def get_popular_items(count):
    request_body = {
        'userEntityId': '<someId>',
        'number': 5
    }

    url = 'http://localhost:8000/queries.json'
    res = request.post(url, data=request_body)
    response_body = None
    if res.status_code == 200:
        response_body = {
            'success': True, 
            'data': res.json()
        }
    else:
        response_body = {
            'success': False,
            'error': res.status_code
        }

    return response_body