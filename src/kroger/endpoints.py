# Import all the necessary packages
import json

import src.database.mongodb.config as mongo
from src.kroger.python_kroger_client.client import KrogerServiceClient
from src.kroger.python_kroger_client.config import encoded_client_token

instanceDB = mongo.getDb().get_database('public')
users_collection = instanceDB['users']
service_client = KrogerServiceClient(encoded_client_token=encoded_client_token)


def locations(zipCode: str, radius: str, limit=10):
    if not zipCode or not radius:
        response = {
            'statusCode': 400,
            'status': False,
            'message': 'Zip Code and Radius is required',
            'data': None
        }
        return response
    result = service_client.get_locations(zipCode, radius, limit)
    response = {
        'statusCode': 200,
        'status': True,
        'message': None,
        'data': {"locations": result}
    }
    return response


def saveLocation(body: dict) -> dict:
    location_id = body.get('location_id', None)
    user_guid = body.get('user_guid', None)
    if not location_id or not user_guid:
        response = {
            'statusCode': 400,
            'status': False,
            'message': 'Location and ID is required',
            'data': None
        }
        return response
    res = users_collection.find_one({'user_guid': user_guid})
    if not res:
        response = {
            'statusCode': 401,
            'status': False,
            'message': 'ID is not valid',
            'data': None
        }
        return response
    newvalues = {"$set": {'location_id': location_id}}
    users_collection.update_one({'user_guid': user_guid}, newvalues)
    response = {
        'statusCode': 200,
        'status': True,
        'message': None,
        'data': None
    }
    return response


def products(body: dict, fulfillment='csp', limit=10):
    user_guid = body.get('user_guid')
    searchTerm = body.get('search_term')
    if not searchTerm or not user_guid:
        response = {
            'statusCode': 400,
            'status': False,
            'message': 'Search Term and ID is required',
            'data': None
        }
        return response
    res = users_collection.find_one({'user_guid': user_guid})
    if not res:
        response = {
            'statusCode': 401,
            'status': False,
            'message': 'ID is not valid',
            'data': None
        }
        return response
    if res.get('location_id', None) is None:
        response = {
            'statusCode': 401,
            'status': False,
            'message': 'Location is not set',
            'data': {
                'location_id': False
            }
        }
        return response
    result = service_client.search_products(term=searchTerm, location_id=res.get('location_id'),
                                            fulfillment=fulfillment,
                                            limit=limit)

    response = {
        'statusCode': 200,
        'status': True,
        'message': None,
        'data': {"products": result}
    }
    return response


def product_details(body: dict):
    user_guid = body.get('user_guid')
    # productId="0004600028732",
    productId = body.get('product_id')
    if not productId or not user_guid:
        response = {
            'statusCode': 400,
            'status': False,
            'message': 'Product ID and ID is required',
            'data': None
        }
        return response
    res = users_collection.find_one({'user_guid': user_guid})
    if not res:
        response = {
            'statusCode': 401,
            'status': False,
            'message': 'ID is not valid',
            'data': None
        }
        return response
    if res.get('location_id', None) is None:
        response = {
            'statusCode': 401,
            'status': False,
            'message': 'Location is not set',
            'data': {
                'location_id': False
            }
        }
        return response
    result = service_client.fetch_product(product_id=productId, location_id=res.get('location_id'))
    response = {
        'statusCode': 200,
        'status': True,
        'message': None,
        'data': {"product_info": result}
    }
    return response
