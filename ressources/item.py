import sqlite3
from flask_restful import Resource,  reqparse
from flask_jwt import  jwt_required

from models.item import ItemModel


class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='this field is required')
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help='every item needs a store id')

    @jwt_required()
    def get(self,name):
        item  = ItemModel.find_item_by_name(name)
        if item :
            return item.json()
        return {'message' : f'item {name} not found !'} ,404

    def post(self , name):
        if  ItemModel.find_item_by_name(name):
            return {'message' : f'item {name} already exists'}, 201
        request_data = Item.parser.parse_args()
        item  = ItemModel( name ,**request_data)
        try :
            item.save_to_db()
        except :
            return {"message" : "internal error occurred"}, 500
        return item.json(), 201

    def delete(self,name):
        item =  ItemModel.find_item_by_name(name)
        if item :
            item.delete_from_db()
        return {'message' : 'item deleted'}

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_item_by_name(name)
        if item :
            item.price = data["price"]
            item.store_id = data["store_id"]
        else :
            item = ItemModel(name, **data)
        item.save_to_db()

        return item.json()


class ItemList(Resource):
    def get(self):
        return { 'items' : [item.json() for item in ItemModel.get_items() ] }
        # we can use map function to apply the lambda function to each item in a list
        #return {'items' : list(map(lambda x: x.json(), ItemModel.get_items()))}