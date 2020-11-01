from werkzeug.security import safe_str_cmp
from models.user import UserModel

# this is a callback which been called each time a login is performed
def authenticate(username , password):
    user = UserModel.find_user_by_name(username)
    if user and  safe_str_cmp(user.password ,password) :
        return user



# this is a callback which is called each time a method calling @jwt_required is called
def identity(payload):
    '''
    The payload['identity'] contains the user's id property that we saved into the JWT when we created it.
    The payload also contains other things, such as when the token was created, when it expires, and more
    Important: the identity function is not called unless we decorate our endpoints with the @jwt_required()
    :param payload: returned from the JWT
    :return: user
    '''
    user_id = payload['identity']
    return  UserModel.find_user_by_id(user_id)