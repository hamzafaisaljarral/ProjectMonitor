import os

from pymongo import MongoClient
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

from flask_restful import Api
from flask_cors import CORS
from database.db import initialize_db
from resources.routes import initialize_routes


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'aSuperSecretKey'
app.config['MONGODB_SETTINGS'] = 'localhost:27017'
# app.config['JWT_TOKEN_LOCATION'] = 'cookies'
# app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)

bcrypt = Bcrypt(app)
jwt = JWTManager(app)

api = Api(app)
cors = CORS(app, resources={r'/*': { 'origins': '*' }})
initialize_db(app)
initialize_routes(api)


