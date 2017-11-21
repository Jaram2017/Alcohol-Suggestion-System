from flask import Flask
from api.controller import controller as api
from view.controller import controller as view
import os
import flask_login
import bcrypt

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(view)

login_manager = flask_login.LoginManager()
login_manager.init_app(app)
