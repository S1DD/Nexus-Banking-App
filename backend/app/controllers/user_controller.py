#!/usr/bin/env python3
from flask import flash
from ..models.user import User
from extensions import db


def get_user_by_id(user_id):
    return User.query.get(user_id)


def update_user_profile(user, form):
    try:
        user.name = form.name.data
        user.email = form.email.data
        user.username = form.username.data
        db.session.commit()
        flash('Your profile has been updated!', 'success')
        return True
    except Exception as e:
        db.session.rollback()
        flash('An error occurred while updating your profile. Please try again.', 'danger')
        return False


def change_user_password(user, current_password, new_password):
    try:
        if not user.check_password(current_password):
            flash('Current password is incorrect.', 'danger')
            return False
        user.set_password(new_password)
        db.session.commit()
        flash('Your password has been changed!', 'success')
        return True
    except Exception as e:
        db.session.rollback()
        flash('An error occurred while changing your password. Please try again.', 'danger')
        return False


def delete_user_account(user):
    try:
        db.session.delete(user)
        db.session.commit()
        flash('Your account has been deleted.', 'success')
        return True
    except Exception as e:
        db.session.rollback()
        flash('An error occurred while deleting your account. Please try again.', 'danger')
        return False
