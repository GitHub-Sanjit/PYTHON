# Let'd define a speed _test decorator
from functools import wraps
from time import time

def speed_test(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        start_time = time()
        result = fn(*args,**kwargs)
        end_time = time()
        print(f"Time Elapsed: {end_time - start_time}")
        return result
    return wrapper

@speed_test
def sum_nums_gen():
    return sum(x for x in range(50000000))

@speed_test
def sum_nums_list():
    return sum([x for x in range(50000000)])

print(sum_nums_gen())
print(sum_nums_list())



# Show Args Decorator Solution
# ignoring all the boilerplate code (the stuff that goes in every decorator function, wraps,e tc.), the important logic is really just:

# print("Here are the args:", args)
# print("Here are the kwargs:", kwargs)
# return fn(*args, **kwargs)
# Here's the complete code:

from functools import wraps

def show_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("Here are the args:", args)
        print("Here are the kwargs:", kwargs)
        return fn(*args, **kwargs)
    return wrapper