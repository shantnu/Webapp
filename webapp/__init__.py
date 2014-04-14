from flask import Flask
from flask.ext.login import LoginManager

webapp = Flask(__name__)
webapp.config.from_object('config')

login_manager = LoginManager()
login_manager.init_app(webapp)

from webapp import views