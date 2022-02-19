from sqlite3 import DatabaseError
from flask import Flask
from dotenv import load_dotenv
import psycopg2
import os
app = Flask(__name__)

load_dotenv()


@app.route("/")
def hello():

    return "Hello World!"


if __name__ == "__main__":
    app.run()
