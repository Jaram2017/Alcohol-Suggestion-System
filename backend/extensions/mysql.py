import pymysql

connections = None

def init_app(app):
    connection = pymysql.connect(host=app.config.DB_HOST,
            user=app.config.DB_USER,
            password=app.config.DB_PASSWORD,
            db=app.config.DB_NAME,
            charset='utf8')

