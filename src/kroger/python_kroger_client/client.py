# Import all the necessary packages
import requests
import json

from python_kroger_client.auth_service import get_client_access_token
from python_kroger_client.api_params import get_mapped_params
from python_kroger_client.models.product import Product
from python_kroger_client.models.location import Location


# Production API URL
API_URL = 'https://api.kroger.com/v1'

class KrogerClient:
    '''
        Base class
    '''
    def _make_get_request(self, endpoint, params=None):
        url     = API_URL + endpoint
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.token}',
        }
        response = requests.get(url, headers=headers, params=params)

        return json.loads(response.text)

    def get_locations(self, zipcode, within_miles=10, limit=5, chain='Kroger'):
        params   = get_mapped_params(locals())
        endpoint = '/locations'
        # Fetch data
        results = self._make_get_request(endpoint, params=params)
        data    = results.get('data')

        return [Location.from_json(location) for location in data]

    def search_products(self, term=None, location_id=None, product_id=None, brand=None, fulfillment='csp', limit=5):
        params   = get_mapped_params(locals())
        endpoint = '/products'
        # Fetch data
        results = self._make_get_request(endpoint, params=params)
        data    = results.get('data')

        return [Product.from_json(product) for product in data]

    def fetch_product(self, product_id=None, location_id=None):
        params   = { "filter.locationId": location_id }
        endpoint = '/products/' + product_id
        # Fetch data
        results = self._make_get_request(endpoint, params=params)
        data    = results.get('data')

        return [Product.from_json1(data)]


class KrogerServiceClient(KrogerClient):
    """ A Kroger API client authenticated with the service credentials
        Has limited functionality to:
            - Search for store location details
            - Search for products
    """
    def __init__(self, encoded_client_token):
        self.token = get_client_access_token(encoded_client_token)