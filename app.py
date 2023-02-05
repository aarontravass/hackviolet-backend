from flask import Flask, Response, request
import os
from dotenv import load_dotenv
import src.auth.auth as auth
load_dotenv()

app = Flask(__name__)



@app.route("/login", methods = ['POST'])
def login():
    print(request.json)
    response = auth.login(request.json)
    return Response(response, status=response.get('statusCode'), mimetype='application/json')




if __name__ == "__main__":
    port = os.getenv('PORT')
    host = os.getenv('HOST')
    app.run(host = host, port = port, debug=True)