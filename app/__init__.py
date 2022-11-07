from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_marshmallow import Marshmallow
import os
from flask_moment import Moment

load_dotenv()
db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")
    app.debug = True
    app.secret_key = "k9A#30XeC6JOAR*L"
    migrate = Migrate(app, db)
    moment = Moment(app)

    db.init_app(app)
    ma.init_app(app)

    from .main import index_blueprint, refresh_data_blueprint

    app.register_blueprint(index_blueprint)
    app.register_blueprint(refresh_data_blueprint)

    return app
