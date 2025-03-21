#!/usr/bin/env python3

from flask import jsonify


def handle_error(error, status_code):
    response = jsonify({'error': str(error)})
    response.status_code = status_code
    return response
