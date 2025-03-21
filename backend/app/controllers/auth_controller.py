#!/usr/bin/env python3
from flask import jsonify, session, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_manager
from backend.app.models.user import User
from extensions import db, Bcrypt


bcrypt = Bcrypt()


def register(data):
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not name or not email or not password:
        return jsonify({"error": "Missing required fields."}), 400

    # Check if user already exists
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "{} already exists".format(email)}), 400

    password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    # Add new user to the database
    user = User(name=name, email=email, password_hash=password_hash)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully", "user_id": user.user_id}), 201


def login(data):
    """
    Authenticate a user and set up session-based login
    :param data:
    :return: Success or error message
    """
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Missing email or password"}), 400

    # Find user by email
    user = User.query.filter_by(email=email).first()
    if not user or not bcrypt.check_password_hash(user.password_hash, password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Log the user in using Flask-Login's login_user function
    login_user(user)

    # Set user_id in session (just in case for additional session management)
    session['user_id'] = user.user_id

    return jsonify({"message": "Login successful", "user_id": user.user_id}), 200


def logout():
    """
    Logs the user out of their account by clearing session data and using Flask-Login's logout_user
    """
    # Log out user using Flask-Login's logout_user function
    logout_user()

    # Clear session data
    session.pop('user_id', None)

    flash('You have been logged out successfully.', 'info')
    return redirect(url_for('login'))


def load_user(user_id):
    """
    This function is used by Flask-Login to load the user object from the session
    :param user_id: The user_id from the session
    :return: The user object or None if user is not found
    """
    return User.query.get(int(user_id))


def get_current_user():
    """
    Get the current authenticated user from the session (using Flask-Login's current_user)
    :return:
    """
    if current_user.is_authenticated:
        return jsonify({"user_id": current_user.user_id,
                        "name": current_user.name,
                        "email": current_user.email}), 200
    else:
        return jsonify({"error": "User not authenticated"}), 401
