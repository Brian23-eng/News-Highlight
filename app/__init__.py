from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstarp = Bootstrap()


#initializing application

app = Flask(__name__,instance_relative_config= True)


#Setting up Configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')


from app import views
