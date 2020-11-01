from flask_restful import Resource , reqparse
import sqlite3

from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='username is required')
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='password is required')

    def post(self):
        data        = UserRegister.parser.parse_args()
        if  UserModel.find_user_by_name(data['username']):
            return {'message' : f'user: <{data["username"]}> already exists'},400
        user = UserModel(**data)
        user.save_to_db()
        return {'message' : 'user created successfully'}, 201


    def get(self):
        users =  UserModel.query.all()
        return {'users' : [user.json() for user in users]}


