#!/usr/bin/env python3
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from backend.app.forms import TransactionForm
from ..models.transaction import Transaction
from extensions import db

transaction_bp = Blueprint('transaction', __name__)


@transaction_bp.route('/add_transaction', methods=['GET', 'POST'])
@login_required
def add_transaction():
    form = TransactionForm()
    if form.validate_on_submit():
        transaction = Transaction(
            amount=form.amount.data,
            description=form.description.data,
            date=form.date.data,
            category=form.category.data,
            user_id=current_user.id
        )
        db.session.add(transaction)
        db.session.commit()
        flash('Transaction added successfully!', 'success')
        return redirect(url_for('transaction.view_transactions'))
    return render_template('add_transaction.html', form=form)
