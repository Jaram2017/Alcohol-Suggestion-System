from flask import current_app as app
import pymysql
import pymysql.cursors

db = pymysql.connect(host=app.config.DB_HOST,
            user=app.config.DB_USER,
            password=app.config.DB_PASSWORD,
            db=app.config.DB_NAME,
            charset='utf8')

class User:
    # ==========================================================================
    def __init__(self, user_id, email=None, passwd_hash=None,
                 authenticated=False):
        self.user_id = user_id
        self.email = email
        self.passwd_hash = passwd_hash
        self.authenticated = authenticated

    # ==========================================================================
    def __repr__(self):
        r = {
            'user_id': self.user_id,
            'email': self.email,
            'passwd_hash': self.passwd_hash,
            'authenticated': self.authenticated,
        }
        return str(r)

    # ==========================================================================
    def can_login(self, passwd_hash):
        return self.passwd_hash == passwd_hash

    # ==========================================================================
    def is_active(self):
        return True

    # ==========================================================================
    def get_id(self):
        return self.user_id

    # ==========================================================================
    def is_authenticated(self):
        return self.authenticated

    # ==========================================================================
    def is_anonymous(self):
        return False

def get_user(username):
    with db.cursor() as cursor:
        sql = 'SELECT * FROM User WHERE Username=' + username
        count = cursor.execute(sql)
        if count == 0:
            return None
        row = cursor.fetchone()
        
        return User(row['Username'], email=row['Email'], passwd_hash=row['Password'])