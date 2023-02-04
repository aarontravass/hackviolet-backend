from flask import Flask
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)



@app.route("/")
def hello_world():
    return ""


if __name__ == "__main__":
    port = os.getenv('PORT')
    host = os.getenv('HOST')
    app.run(host = host, port = port)