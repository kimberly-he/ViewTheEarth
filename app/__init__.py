from flask import Flask
import os
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'postgresql://localhost/view_the_earth_dev')

db = SQLAlchemy(app)


def create_app():
    from app.bot import bot as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
