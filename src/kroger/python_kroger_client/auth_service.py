# Import all the necessary packages
import requests
import json
import simple_cache


# Production API URL
API_URL = 'https://api.kroger.com/v1'

@simple_cache.cache_it("access_token.cache", 1800)
def get_client_access_token(encoded_client_token):
    url    = API_URL + '/connect/oauth2/token'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': f'Basic {encoded_client_token}',
    }
    payload = {
        'grant_type':"client_credentials",
        'scope':['product.compact'],
    }
    response = requests.post(url, headers=headers, data=payload)

    return json.loads(response.text).get('access_token')