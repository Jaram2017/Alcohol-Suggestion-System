import flask
from flask import current_app as app
from flask import request
from app import login_manager
from User import User
from User import get_user
from flask_login import login_user, logout_user, current_user, login_required
import hashlib

controller = flask.Blueprint('auth', __name__, template_folder='templates')

@controller.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    user_data = get_user(username)
    if user_data == None:
        return {'success': False, 'error': 'No such user'}
    SHA = hashlib.sha256()
    SHA.update(request.form['password'])
    hash = SHA.hexdigest()

    if user_data.can_login(hash):
        pass
        # WIP