from functools import wraps

def ensure_no_kwargs(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        if kwargs:
            raise ValueError("No Kwargs allowed ! sorry :(")
        return fn(*args,**kwargs)
    return wrapper

@ensure_no_kwargs
def greet(name):
    print(f"hi there {name}")
    
greet(name="Tony")


# Double Return Decorator
# Most of this function is decorator boilerplate...

from functools import wraps

def double_return(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        #logic goes in here...
        return wrapper

# This wrapper function simply runs the function, and returns a list containing the result twice:



from functools import wraps

def double_return(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        val = fn(*args, **kwargs)
        return [val, val]
    return wrapper



# Ensure Fewer Than Three Args Decorator Solution



from functools import wraps

def ensure_fewer_than_three_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if len(args) < 3:
            return fn(*args, **kwargs)
        return "Too many arguments!"
    return wrapper



# Only Ints Decorator Exercise
from functools import wraps

def only_ints(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        if any([arg for arg in args if type(arg) != int]):
            return "Please only invoke with integers."
        return fn(*args, **kwargs)
    return inner



# Ensure Authorized Decorator Solution
from functools import wraps

def ensure_authorized(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs.get("role") == "admin":
            return fn(*args, **kwargs)
        return "Unauthorized"
    return wrapper