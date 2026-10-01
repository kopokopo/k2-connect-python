from functools import wraps
from flask import flash, redirect, url_for
import k2connect
import os

BASE_URL = os.environ.get('BASE_URL')

def handle_k2_errors(anchor):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except Exception as error:
                flash(str(error), "danger")
                return redirect(url_for("index", _anchor=anchor))
        return wrapper
    return decorator


def generate_k2_token(f):
    @wraps(f)
    def wrapper(*args, **kwargs):

        k2connect.initialize(os.environ['CLIENT_ID'], os.environ['CLIENT_SECRET'], BASE_URL)
        token_service = k2connect.Tokens
        access_token_response = token_service.request_access_token()
        os.environ['ACCESS_TOKEN'] = token_service.get_access_token(access_token_response)
        return f(*args, **kwargs)
    return wrapper
