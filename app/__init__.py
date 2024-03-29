from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
REMOTE_HOST = "https://pyecharts.github.io/assets/js"
app.config.from_object('config')
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = "index"
login_manager.init_app(app)
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

from app import routes, models
