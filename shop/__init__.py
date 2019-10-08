from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from shop.config import DevConfig

app=Flask(__name__)
app.config.from_object(DevConfig)

db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)

from shop import views
