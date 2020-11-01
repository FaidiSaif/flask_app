import sqlite3
from db import db

class UserModel(db.Model) :
    """ a model is a helper class to represent the resource
    in this example, a user is a class with (id, username, password)

    a resource is directly interacting with the API through (get, post, delete ...) methods
    """
    __tablename__ = "users"
    id = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self  , username , password):
        self.username   = username
        self.password   = password

    def json(self):
        return {'username' : self.username , 'passwd' :  '*********'}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_user_by_name(cls, username):
        return cls.query.filter_by(username = username).first()

    @classmethod
    def find_user_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def get_users(cls):
        return cls.query.all()