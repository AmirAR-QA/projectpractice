from application import app
from application import app
from flask import Flask

app = Flask(__name__)

from application import routes

if __name__=="__main__": app.run(port=5002, host='0.0.0.0', debug=True)  