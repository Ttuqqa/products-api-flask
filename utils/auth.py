import jwt

from functools import wraps
from flask import request

from utils.secrets import SECRET_KEY


def token_required(func):

    @wraps(func)
    def decorated(*args, **kwargs):

        token = request.headers.get('Authorization')

        if not token:

            return {
                'success': False,
                'error': 'token is missing'
            }, 401

        try:

            jwt.decode(
                token,
                SECRET_KEY,
                algorithms=['HS256']
            )

        except:

            return {
                'success': False,
                'error': 'invalid token'
            }, 401

        return func(*args, **kwargs)

    return decorated