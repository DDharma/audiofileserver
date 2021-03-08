from flask import Flask,request
from flask_cors import CORS,cross_origin
import json, datetime

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

from routes import apis   
from modules import connection  