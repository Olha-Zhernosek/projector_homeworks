from functools import wraps


'''2. Write a decorator that wraps a function in a try-except
block and prints an error if any type of error has happened.
Example:

@catch_errors
def some_function_with_risky_operation(data):
    print(data['key'])

some_function_with_risky_operation({'foo': 'bar'})
> Found 1 error during execution of your function: KeyError no such key as foo

some_function_with_risky_operation({'key': 'bar'})
> bar'''


def catch_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            print(f"Found 1 error during execution of your function: KeyError no such key as {e}")

    return wrapper


@catch_errors
def some_function_with_risky_operation(data):
    print(data['foo'])


def main():
    some_function_with_risky_operation({'foo': 'bar'})
    some_function_with_risky_operation({'key': 'bar'})


if __name__ == "__main__":
    main()
