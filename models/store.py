from db import db

class StoreModel(db.Model) :

    __tablename__ = "stores"
    id      = db.Column(db.Integer , primary_key = True)
    name    = db.Column(db.String(80))
    items   = db.relationship('ItemModel'  , lazy = 'dynamic')
    #lazy = dynamic tells sqlalchemy to not create an ItemModel object for each item having the store_id of this store
    #since it's expensive if there is many stores and many items and in this case the items is not a list of objects anymore
    # but a query allowing access to the items table

    def __init__(self, name ):
        self.name       = name

    def json(self):
        ''' since the lazy option is set to dynamic, the json method takes a lot of time to execute because it access the database for each call
        '''
        return {'name' : self.name , 'items' : [item.json() for item in self.items.all()]}

    @classmethod
    def find_store_by_name(cls,name):
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
    def get_stores(cls):
        return cls.query.all()

