from application import app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = "secret"

db = SQLAlchemy(app)

from application import routes

if __name__=="__main__": app.run(port=5003, host='0.0.0.0', debug=True)  