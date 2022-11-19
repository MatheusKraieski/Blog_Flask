from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'bcc9bdc83147456ebd8da8bfe5eec301'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from app import routes