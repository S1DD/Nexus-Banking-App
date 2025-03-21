#!/usr/bin/env python3
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user
from backend.app.controllers.auth_controller import login

# Create a Blueprint for authentication routes
auth_bp = Blueprint('auth', __name__)


# Root route that shows the login page
@auth_bp.route('/')
def index():
    return render_template('signup.html')


# Login route
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = login(email, password)
        if user:
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('dashboard'))  # Redirect to the dashboard after login
        else:
            flash('Invalid email or password.', 'danger')
    return render_template('login.html')


# Logout route
@auth_bp.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('auth.login'))
