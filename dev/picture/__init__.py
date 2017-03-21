import os

from flask import Flask
from flask_login import LoginManager



#Configure authentication
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.init_app(app)