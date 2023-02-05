import src.database.mongodb.config as mongo
import bcrypt
import jwt
import hashlib
import uuid
import json

instanceDB = mongo.getDb().get_database('public')

users_collection = instanceDB['users']
authTable = instanceDB['auth_token']


# def addUser(body) -> dict:
#     response = {}
#     mongo_res = users_collection.find({'email': body.get('email')})


def login(body: dict) -> dict:
    email = body.get('email')
    password = body.get('password')
    if email is None or password is None:
        response = {
            'statusCode': 400,
            'status': False,
            'message': 'Email and Password is required'
        }
        return response
    hashed_string = hashlib.sha384(password.encode('utf-8')).hexdigest()

    mongo_res = users_collection.find_one({'email': email})
    if mongo_res is None:
        response = {
            'statusCode': 401,
            'message': 'Invalid User Credentials',
            'status': False
        }
        return response
    if not bcrypt.checkpw(hashed_string.encode('utf-8'), mongo_res.get('password').encode('utf-8')):
        response = {
            'statusCode': 401,
            'message': 'Invalid Password',
            'status': False
        }
        return response
    payload = {
        'user_guid': mongo_res['user_guid']
    }
    auth_token = jwt.encode(payload, key="secret", algorithm="HS256")
    insert_body = {
        'auth_token': auth_token,
        'user_guid': mongo_res['user_guid']
    }

    authTable.insert_one(insert_body);
    response = {
        'statusCode': 200,
        'message': None,
        'status': True,
        'data': {
            'auth_token': auth_token,
            'user_guid': mongo_res['user_guid']
        }
    }
    print(response)

    return response


def register(body: dict) -> dict:
    first_name = body.get('first_name')
    last_name = body.get('last_name')
    email = body.get('email')
    password = body.get('password')
    if not first_name or not last_name or not email or not password:
        response = {
            'statusCode': 400,
            'status': False,
            'message': 'First Name, Last Name, Email, Password is required'
        }
        return response
    hashed_string = hashlib.sha384(password.encode('utf-8')).hexdigest()
    hashed = bcrypt.hashpw(hashed_string.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    input_data = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': hashed,
        'user_guid': str(uuid.uuid4())
    }
    users_collection.insert_one(input_data)
    response = {
        'statusCode': 200,
        'status': True,
        'message': 'Successfully inserted',
        'data': None
    }
    return response


def logout(body: dict, authHeader: str) ->dict:
    if not authHeader:
        response = {
            'statusCode': 401,
            'status': False,
            'message': 'Invalid ID or token',
            'data': None
        }
        return response;
    auth_token = authHeader.split(' ')
    if(len(auth_token) == 1):
        response = {
            'statusCode': 401,
            'status': False,
            'message': 'Invalid ID or token',
            'data': None
        }
        return response;
    auth_token = auth_token[1]
    user_guid = body.get('user_guid')
    res = authTable.find_one({'user_guid':user_guid, 'auth_token':auth_token})
    if not res:
        response = {
            'statusCode': 401,
            'status': False,
            'message': 'Invalid ID or token',
            'data': None
        }
        return response;
    res = authTable.delete_one({'user_guid':user_guid, 'auth_token':auth_token})
    if res.deleted_count == 1:
        response = {
            'statusCode': 200,
            'status': True,
            'message': 'Logout Successfull',
            'data': None
        }
        return response;
    response = {
        'statusCode': 500,
        'status': False,
        'message': 'Something went wrong',
        'data': None
    }
    return response;

