from flask import Blueprint, request, jsonify
from backend.app.controllers.auth_controller import register, login, get_current_user

auth_routes = Blueprint('auth', __name__)


@auth_routes.route('/register', methods=['POST'])
def register_route():
    """
    Register a new user.
    """
    data = request.get_json()
    return register(data)


@auth_routes.route('/login', methods=['POST'])
def login_route():
    """
    Authenticate a user and return a JWT token.
    """
    data = request.get_json()
    return login(data)


@auth_routes.route('/me', methods=['GET'])
def get_current_user_route():
    """
    Get the current authenticated user.
    """
    return get_current_user()
