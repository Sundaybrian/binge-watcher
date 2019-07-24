#where we will initialize our application

from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

#initializing application
app = Flask(__name__,instance_relative_config = True)

#setting up config
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py') #hooking up our config to the api key file

#Intiliazing Flask Extensions
bootstrap = Bootstrap(app)


from app import views
from app import error