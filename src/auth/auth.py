import src.database.mongodb.config as mongo
import bcrypt
import jwt

instanceDB = mongo.getDb().get_database('public')


users_collection = instanceDB['users']
authTable = instanceDB['auth_token']


# def addUser(body) -> dict:
#     response = {}
#     mongo_res = users_collection.find({'email': body.get('email')})


def login(body: dict) -> dict:
    response = {}
    email = body.get('email')
    password = body.get('password')
    if email is None or password is None:
        response = {
            'statusCode': 400,
            'message': 'Email and Password is required'
        }
        return response
    hashed = bcrypt.hashpw(str.encode(password), bcrypt.gensalt()).decode('utf-8')
    mongo_res = users_collection.find_one({'email': email, 'password': hashed})
    if mongo_res is None:
        response = {
            'statusCode': 401,
            'message': 'Invalid User Credentials'
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
        'data': insert_body
    }
    return response



{
    "search_term":"taco",
    "ser_guid":'abcd',
}