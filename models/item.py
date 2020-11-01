import sqlite3
from db import db

class ItemModel(db.Model) :

    __tablename__ = "items"
    id      = db.Column(db.Integer , primary_key = True)
    name    =  db.Column(db.String(80))
    price   = db.Column(db.Float(precision = 2) )

    store_id= db.Column(db.Integer , db.ForeignKey('stores.id'))
    store   = db.relationship('StoreModel')

    def __init__(self, name , price , store_id):
        self.name       = name
        self.price      = price
        self.store_id   = store_id

    def json(self):
        return {'name' : self.name , 'price' : self.price, 'store_id':  self.store_id}

    @classmethod
    def find_item_by_name(cls,name):
        return cls.query.filter_by(name = name).first()
        # the sqlAlchemy can convert a column from the db to an object for us
        # in this method we can call filter_by many times on the same query, or pass many params for filtering like(name=name , id=id )

    def save_to_db(self):
        """this method replace the update and the insert methods
        """
        db.session.add(self) #if the id already exists it makes an update else it add a new element to the db
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_items(cls):
        return cls.query.all()

