from functools import wraps

'''1. Write a decorator that ensures a function is only
called by users with a specific role. Each function should
have an user_type with a string type in kwargs.

@is_admin
def show_customer_receipt(user_type: str):
    # Some very dangerous operation

show_customer_receipt(user_type='user')
> ValueError: Permission denied

show_customer_receipt(user_type='admin')
> function pass as it should be'''


def is_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user_type = kwargs.get('user_type')

        if user_type == 'admin':
            return func(*args, **kwargs)
        else:
            raise ValueError("Permission denied for non-admin users")
    return wrapper


@is_admin
def show_customer_receipt(user_type: str):
    # Some very dangerous operation
    return "function pass as it should be"


try:
    result2 = show_customer_receipt(user_type='user')
except ValueError as error:
    print(error)

result1 = show_customer_receipt(user_type='admin')
print(result1)
