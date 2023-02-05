from flask import Flask, Response, request
import os
from dotenv import load_dotenv
import src.auth.auth as auth
import json
load_dotenv()

app = Flask(__name__)



@app.route("/login", methods = ['POST'])
def login():
    print(request.json)
    res = auth.login(request.json)
    return Response(response=json.dumps(res), status=res.get('statusCode'), mimetype='application/json')

@app.route("/register", methods = ['POST'])
def register():
    print(request.json)
    res = auth.register(request.json)
    return Response(response=json.dumps(res), status=res.get('statusCode'), mimetype='application/json')

@app.route("/logout", methods = ['POST'])
def logout():
    authHeader = request.headers.get('Authorization')
    res = auth.logout(request.json, authHeader)
    return Response(response=json.dumps(res), status=res.get('statusCode'), mimetype='application/json')


if __name__ == "__main__":
    port = os.getenv('PORT')
    host = os.getenv('HOST')
    app.run(host = host, port = port, debug=True)