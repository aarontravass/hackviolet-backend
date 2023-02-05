# Import all the necessary packages
import base64

# Get these 3 values from registering your developer account/application with https://developer.kroger.com/
client_id     = 'hackviolet23-d5777aed77e91b1d981a426eb57347d83948257829297173864'
client_secret = 'T53Tk6KemXTMQ5DniMFZhhWHI6soS0wPkO0LHeMu'
redirect_uri  = 'http://localhost:5000'

# Authentication requires base64 encoded id:secret, which is precalculated here
encoded_client_token = base64.b64encode(f"{client_id}:{client_secret}".encode('ascii')).decode('ascii')