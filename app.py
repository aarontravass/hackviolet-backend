from flask import Flask
import os
from dotenv import load_dotenv
import src.kroger.kroger as kroger
load_dotenv()

app = Flask(__name__)



@app.route("/")
def hello_world():
    return ""


@app.route("/kroger/location_id")
def getLocation(zip_code: str):
    return kroger.location(zip_code)

if __name__ == "__main__":
    port = os.getenv('PORT')
    host = os.getenv('HOST')
    app.run(host = host, port = port)