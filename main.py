from flask import Flask
from flask_restful import  Api
from flask_jwt import JWT


from db import db
from security import authenticate,identity
from ressources.user import UserRegister
from ressources.item import Item , ItemList
from ressources.store import Store , StoreList
#importinh Store , Item

app             = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]   =   'sqlite:///data.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# the line above : deactivate the extension (flask_SQLAlchemy) tracker to save resources
# but doesn't deactivate the underlying SQLAlchemy tracker
app.secret_key  = 'XXX156Ye54'
api             = Api(app)
jwt             = JWT(app,authenticate,identity)

@app.before_first_request
def create_tables():
    ''' this uses all the subclasses of the db.Model to create the tables
    '''
    db.create_all()



api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

api.add_resource(UserRegister, '/register')

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug = True)


