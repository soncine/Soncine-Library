from functools import wraps
from flask import request, redirect

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in request.session:
            return redirect('/login')
        return f(*args, **kwargs)
    
    return decorated_function