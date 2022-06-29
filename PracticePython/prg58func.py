from functools import wraps


def decorator(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        """Decorator's docstring"""
        return f(*args, **kwargs)

    print('Documentation of decorated :', decorated.__doc__)
    return decorated


@decorator
def f(x):
    """f's Docstring"""
    return x


print('f name :', f.__name__)
print('Documentation of f :', f.__doc__)