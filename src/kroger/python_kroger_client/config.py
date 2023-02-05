# Import all the necessary packages
import base64
import os
from dotenv import load_dotenv
load_dotenv()
# Get these 3 values from registering your developer account/application with https://developer.kroger.com/
client_id     = os.getenv('KROGER_CLIENT_ID')
client_secret = os.getenv('KROGER_CLIENT_SECRET')
redirect_uri  = os.getenv('KROGER_REDIRECT_URI')

# Authentication requires base64 encoded id:secret, which is precalculated here
encoded_client_token = base64.b64encode(f"{client_id}:{client_secret}".encode('ascii')).decode('ascii')