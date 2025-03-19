#!/usr/bin/python3
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy


# Initialize extensions
db = SQLAlchemy()


def create_app():
    # Create the Flask app instance
    app = Flask(__name__)

    # Load configurations
    app.config.from_pyfile('config.py')

    # Configure MySQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"mysql+pymysql://{app.config['MYSQL_USER']}:{app.config['MYSQL_PASSWORD']}@"
        f"{app.config['MYSQL_HOST']}:{app.config['MYSQL_PORT']}/{app.config['MYSQL_DB']}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)

    return app
