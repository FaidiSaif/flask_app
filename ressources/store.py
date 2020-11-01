from flask_restful import Resource,  reqparse
from models.store import StoreModel

class Store(Resource):

    def get(self, name):
        store = StoreModel.find_store_by_name(name)
        if store :
            return store.json(), 200
        else :
            return {'message': f"store {name} does not exist"}, 404

    def post(self,name):
        store = StoreModel.find_store_by_name(name)
        if store :
            return {'message' : f"store {name} already exists"}
        else :
            store = StoreModel(name)
            try :
                StoreModel.save_to_db(store)
            except :
                return {'message' : 'An error occurred while creating the store'},500
        return store.json() ,201

    def delete(self,name):
        store = StoreModel.find_store_by_name(name)
        if store :
           try :
               StoreModel.delete_from_db(store)
           except :
               return {'message' :  'error occurred while deleting the store'} , 500
        return {'message' : 'store deleted successfully'}



class StoreList(Resource):
    def get(self):
        return {'stores' :  [store.json() for store in StoreModel.get_stores()]}
