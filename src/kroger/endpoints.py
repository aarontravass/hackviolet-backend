# Import all the necessary packages
import json

import src.database.mongodb.config as mongo
from python_kroger_client.client import KrogerServiceClient
from python_kroger_client.config import encoded_client_token

instanceDB       = mongo.getDb().get_database('public')
users_collection = instanceDB['users']
service_client   = KrogerServiceClient(encoded_client_token=encoded_client_token)


def locations(zipCode=24060, within_miles=10, limit=10):
    result = service_client.get_locations(zipCode, within_miles, limit)

    return json.dumps({"locations": result})

def getLocationId(user_guid: str) -> str:
    user = users_collection.find_one({'user_guid': user_guid})

    return user.get('location_id')

def products(body: dict, fulfillment='csp', limit=10):
    locationId = getLocationId(body.get('user_guid'))
    searchTerm = body.get('search_term')
    result     = service_client.search_products(term=searchTerm, location_id=locationId, fulfillment=fulfillment, limit=limit)

    return json.dumps({"products": result})

def product_details(body: dict, productId="0004600028732", locationId="01400376"):
    locationId = getLocationId(body.get('user_guid'))
    result     = service_client.fetch_product(product_id=productId, location_id=locationId)

    return json.dumps({"product_info": result})