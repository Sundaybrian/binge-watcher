#where we will initialize our application

from flask import Flask
from .config import DevConfig

#initializing application
app = Flask(__name__)

#setting up config

app.config.from_object(DevConfig)
app.config.from_pyfile('config.py') #hooking up our config to the api key file


from app import views