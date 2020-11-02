from functools import wraps


def double_return(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return [fn(*args, **kwargs), fn(*args, **kwargs)]
    return wrapper

# can put fn(*args, **kwargs) into a variable
# def double_return(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         val = fn(*args, **kwargs)
#         return [val, val]
#     return wrapper
