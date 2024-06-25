from datetime import datetime
from functools import wraps


def time(func):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        t1 = datetime.now()
        result = func(*args, **kwargs)
        t2 = datetime.now()
        x = t2 - t1
        result = [x.microseconds/1000.0] + result # [f"time was {x.microseconds/1000.0} miliseconds"] 
        return result

    return wrapper