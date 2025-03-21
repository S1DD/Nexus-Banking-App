#!/usr/bin/env python3
from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, DecimalField, DateField, SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from ..app.models.user import User


# Signup Form
class SignupForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    # Custom validation to check if email or username already exists
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exists. Please choose another.')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists. Please choose another.')


# Login Form
class LoginForm(FlaskForm):
    email_or_username = StringField('Email or Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


# Profile Form
def validate_username(username):
    if username.data != current_user.username:
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists. Please choose another.')


def validate_email(email):
    if email.data != current_user.email:
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exists. Please choose another.')


class ProfileForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    submit = SubmitField('Update Profile')

class ChangePasswordForm(FlaskForm):
    current_password = PasswordField('Current Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm New Password', validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Change Password')


# Transaction Form
class TransactionForm(FlaskForm):
    amount = DecimalField('Amount', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired(), Length(max=200)])
    date = DateField('Date', validators=[DataRequired()])
    category = SelectField('Category', choices=[
        ('groceries', 'Groceries'),
        ('rent', 'Rent'),
        ('entertainment', 'Entertainment'),
        ('transport', 'Transport'),
        ('other', 'Other')
    ], validators=[DataRequired()])
    submit = SubmitField('Add Transaction')

# Budget Form
class BudgetForm(FlaskForm):
    category = SelectField('Category', choices=[
        ('groceries', 'Groceries'),
        ('rent', 'Rent'),
        ('entertainment', 'Entertainment'),
        ('transport', 'Transport'),
        ('other', 'Other')
    ], validators=[DataRequired()])
    amount = DecimalField('Amount', validators=[DataRequired()])
    submit = SubmitField('Set Budget')