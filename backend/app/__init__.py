from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
cors = CORS()


def create_app():
    """
    Factory function to create and configure Flask app.
    :return: App instance
    """
    # Create the Flask app instance
    app = Flask(__name__)

    # Load the configurations
    app.config.from_pyfile('config.py')

    # Initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    cors.init_app(app)

    # Register blueprints (routes)
    from backend.app.routes.auth_routes import auth_routes
    from backend.app.routes.transaction_routes import transaction_routes
    from backend.app.routes.user_routes import user_routes

    app.register_blueprint(auth_routes)
    app.register_blueprint(transaction_routes)
    app.register_blueprint(user_routes)

    # (Optional) Add error handlers
    register_error_handlers(app)

    return app


def register_error_handlers(app):
    """
    Register custom error handlers for the app.
    """

    @app.errorhandler(404)
    def not_found(error):
        return {"error": "Resource not found"}, 404

    @app.errorhandler(500)
    def internal_error(error):
        return {"error": "Internal server error"}, 500
