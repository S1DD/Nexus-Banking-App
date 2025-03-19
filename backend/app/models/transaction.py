import uuid
from datetime import datetime
from uuid import uuid4
from backend.app.models.user import User
from app import db


class Transaction(db.Model):

    __tablename__ = 'transactions'

