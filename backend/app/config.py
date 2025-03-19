"""Configurations parameters for MySQL database, Plaid and session management"""
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv()

# MYSQL Configurations
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_DB = os.getenv("MYSQL_DB")

# PLAID Configuration
PLAID_CLIENT_ID = os.getenv("PLAID_CLIENT_ID")
PLAID_ENV = os.getenv('PLAID_ENV', 'sandbox')
