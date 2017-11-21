import flask
from extensions import mysql

app = flask.Flask(__name__)

app.config['DB_HOST'] = 'localhost'
app.config['DB_USER'] = 'test'
app.config['DB_PASSWORD'] = 'q1w2e3r4'
app.config['DB_NAME'] = 'alcohol'
app.config['APP_NAME'] = 'AlcoholPrediction'
app.config['ACCESSKEY'] = 'ayQOHAKcaEvSTI-Qrv1HjW-XDPE7dgRyit6oEFoM3fAaEKPdwe4zFQe19jGow271'
mysql.init_app(app)

