#!/usr/bin/env python3
from extensions import login_manager, bcrypt, migrate, db
from backend.app.models.user import User
from flask import Flask
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def create_app():
    # Create the Flask app
    app = Flask(__name__)

    # Load configuration from environment variables or config file
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///nexus.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions with the app
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    # Configure login manager
    login_manager.login_view = 'login.html'  # Route for login page
    login_manager.login_message_category = 'info'  # Bootstrap class for login messages

    # Define the user_loader callback
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    # Register blueprints
    from backend.app.routes.auth_routes import auth_bp
    from backend.app.routes.user_routes import user_bp
    from backend.app.routes.transaction_routes import transaction_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(transaction_bp)

    # Create database tables (if they don't exist)
    with app.app_context():
        db.create_all()

    # Return the app instance at the end
    return app


# Create the app instance
app = create_app()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
