#!/usr/bin/env python3
from extensions import db
from datetime import datetime


class Transaction(db.Model):
    """
    Represents a financial transaction in the database.
    """
    __tablename__ = 'transactions'

    transaction_id = db.Column(db.Integer, primary_key=True)  # Primary key
    amount = db.Column(db.Float, nullable=False)  # Transaction amount
    description = db.Column(db.String(200), nullable=False)  # Transaction description
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)  # Transaction date
    category = db.Column(db.String(50), nullable=False)  # Transaction category (e.g., groceries, rent)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)  # Foreign key to User

    # Relationship to User model
    user = db.relationship('User', backref=db.backref('transactions', lazy=True))

    def __repr__(self):
        return f"Transaction(id={self.id}, amount={self.amount}, description={self.description}, date={self.date}, category={self.category})"

