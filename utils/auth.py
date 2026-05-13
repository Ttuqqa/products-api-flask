import jwt

from functools import wraps
from flask import request

from utils.secrets import SECRET_KEY


def token_required(func):

    @wraps(func)
    def decorated(*args, **kwargs):

        auth_header = request.headers.get('Authorization')

        if not auth_header:

            return {'success': False,'error': 'token is missing' }, 401
            
        parts= auth_header.split()
        
        if len(parts) !=2 or parts[0]!='Bearer':
          return{'success':False, 'error':'invalid token format'},401
        
        token= parts[1]

        try:

            data=jwt.decode(
                token,
                SECRET_KEY,
                algorithms=['HS256']
            )
            request.current_user= data['username']

        except:

            return {'success': False,'error': 'invalid token'}, 401

        return func(*args, **kwargs)

    return decorated