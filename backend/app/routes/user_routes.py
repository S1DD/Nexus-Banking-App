#!/usr/bin/env python3
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from ..forms import ProfileForm, ChangePasswordForm
from ..controllers.user_controller import update_user_profile, change_user_password, delete_user_account

user_bp = Blueprint('user', __name__)

@user_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm()
    if form.validate_on_submit():
        if update_user_profile(current_user, form):
            return redirect(url_for('user.profile'))
    form.name.data = current_user.name
    form.email.data = current_user.email
    form.username.data = current_user.username
    return render_template('profile.html', form=form)

@user_bp.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if change_user_password(current_user, form.current_password.data, form.new_password.data):
            return redirect(url_for('user.profile'))
    return render_template('change_password.html', form=form)

@user_bp.route('/delete_account', methods=['POST'])
@login_required
def delete_account():
    if delete_user_account(current_user):
        return redirect(url_for('auth.logout'))
    return redirect(url_for('user.profile'))