from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from sqlalchemy.sql import func

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    posts = db.relationship('Post', backref = 'user', lazy = "dynamic", passive_deletes=True)

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class Quote:
    '''
    Quote class to define Quote objects
    '''

    def __init__(self, author, id, quote):
        self.author = author
        self.id = id
        self.quote = quote

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key = True)
    date_created = db.Column(db.DateTime(timezone = True), default = func.now())
    content = db.Column(db.String(), nullable=False)
    author = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    

    def __repr__(self):
        return f'{self.date_created}'