from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from backend.app.forms import ProfileForm
from backend.app.models import User, db

# Create a Blueprint for user routes
user_bp = Blueprint('user', __name__)

# Profile Route
@user_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm()
    if form.validate_on_submit():
        # Update user profile
        current_user.name = form.name.data
        current_user.email = form.email.data
        current_user.username = form.username.data

        # Save changes to the database
        db.session.commit()
        flash('Your profile has been updated!', 'success')
        return redirect(url_for('user.profile'))

    # Pre-fill the form with current user data
    form.name.data = current_user.name
    form.email.data = current_user.email
    form.username.data = current_user.username

    return render_template('profile.html', form=form)

# View User Details Route
@user_bp.route('/user/<int:user_id>')
@login_required
def view_user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('view_user.html', user=user)