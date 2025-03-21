#!/usr/bin/env python3
"""Configurations parameters for MySQL database and session management"""
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
