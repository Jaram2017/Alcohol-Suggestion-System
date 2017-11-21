from flask import Blueprint
from flask import request
from flask import current_app as app
import pymysql
import requests

controller = Blueprint('liquors', __name__, template_folder='templates')

db = pymysql.connect(host=app.config.DB_HOST,
            user=app.config.DB_USER,
            password=app.config.DB_PASSWORD,
            db=app.config.DB_NAME,
            charset='utf8')

accessKey = app.config.ACCESSKEY
@controller.route('/', methods=['GET'])
def get_liquors():
    data = None
    with db.cursor() as cursor:
        sql = 'SELECT ID FROM Liquor'
        cursor.execute(sql)
        data = cursor.fetchall()
    if data == None:
        return []
    data = list(map(lambda a: a[0], data))
    return data

@controller.route('/<id>', methods=['GET'])
def get_liquor(id):
    columns = ['id', 'name', 'price', 'description', 'category']
    data = None
    res = {'success': False, 'error': ''}
    
    if not id.isdigit():
        res['error'] = 'Not a valid id type!'
        return res
    
    with db.cursor() as cursor:
        sql = 'SELECT l.ID, l.Name, Price, Description, c.Name as Category FROM Liquor as l, Category as c ON l.Category = c.ID  WHERE id={}'.format(id)
        cursor.execute(sql)
        data = cursor.fetchall()

    data = data[0]
    data = dict(map(lambda x, y: (x, y), columns, data))
    res['success'] = True
    res = {**res, **data}
    return res

@controller.route('/<id>/like', methods=['POST'])
def like_liquor(id):
    request_body = {
        'event': 'view',
        'entityId': '<someid>',
        'entityType': 'user',
        'targetEntityType': 'item', 
        'targetEntityId': id
    }

    url = 'http://localhost:7070/events.json?accessKey=' + accessKey
    res = request.post(url, data=request_body)
    if res.status_code == 200:
        return {'success': True}
    else:
        return {'success': False, 'error': str(res.status_code)}

@controller.route('/<id>/buy', methods=['POST'])
def buy_liquor(id):
    request_body = {
        'event': 'buy',
        'entityId': '<someid>',
        'entityType': 'user',
        'targetEntityType': 'item', 
        'targetEntityId': id
    }

    url = 'http://localhost:7070/events.json?accessKey=' + accessKey
    res = request.post(url, data=request_body)
    if res.status_code == 200:
        return {'success': True}
    else:
        return {'success': False, 'error': str(res.status_code)}

