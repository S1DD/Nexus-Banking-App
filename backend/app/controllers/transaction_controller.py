#!/usr/bin/env python3
from flask import flash
from ..models import Transaction
from extensions import db


def add_transaction(user, form):
    """
    Adds a new transaction for the user.
    """
    transaction = Transaction(
        amount=form.amount.data,
        description=form.description.data,
        date=form.date.data,
        category=form.category.data,
        user_id=user.id
    )

    # Add transaction to the database
    db.session.add(transaction)
    db.session.commit()
    flash('Transaction added successfully!', 'success')
    return True