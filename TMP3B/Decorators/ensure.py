from functools import wraps


def ensure_no_kwargs(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError('No Kwargs allowed.')
        return fn(*args, **kwargs)
    return wrapper


@ensure_no_kwargs
def greet(name):
    print(f'hello {name}')


greet(name="Tony")
