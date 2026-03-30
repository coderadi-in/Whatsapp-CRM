'''coderadi &bull; Main file for the Project.'''

# ? IMPORTING LIBRARIES
from flask import Flask
import os
from router import router
from plugins import *

# ! LOAD VIRTUAL ENVIRONMENT
from dotenv import load_dotenv
load_dotenv('.venv/vars.env')

# ! INITIALIZING SERVER
server = Flask(__name__)
server.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
server.config['SECRET_KEY'] = os.getenv('KEY')

# ! BIND PLUGINS
db.init_app(server)
server.register_blueprint(router)

# ! INITIALIZE DATABASE
with server.app_context():
    db.create_all()