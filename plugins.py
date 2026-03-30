'''coderadi &bull; Plugins management file for the Project.'''

# ? IMPORTS
from flask_sqlalchemy import SQLAlchemy
import os
from twilio.rest import Client

# ! ENV FETCH
account_sid = os.getenv('SID')
auth_token = os.getenv('TOKEN')

# ! INITIALIZATION
db = SQLAlchemy()
client = Client(account_sid, auth_token)

# | MESSAGES DATABASE MODEL
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    body = db.Column(db.TEXT, nullable=False)
    sender = db.Column(db.String, nullable=False)