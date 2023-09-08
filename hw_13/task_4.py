import time

'''5. Optional: Write a decorator that adds a rate-limiter
to a function, so that it can only be called a certain amount
of times per minute '''


def rate_limit_decorator(limit_per_minute):
    def decorator(func):
        last_called = 0
        calls_in_current_minute = 0

        def wrapper(*args, **kwargs):
            nonlocal last_called, calls_in_current_minute

            current_time = time.time()

            if current_time - last_called >= 60:
                calls_in_current_minute = 0

            if calls_in_current_minute < limit_per_minute:
                last_called = current_time
                calls_in_current_minute += 1
                return func(*args, **kwargs)
            else:
                raise Exception(f"Досягнуто обмеження на кількість "
                                f"викликів ({limit_per_minute}) "
                                f"за хвилину.")

        return wrapper

    return decorator


@rate_limit_decorator(5)
def my_function():
    # функція
    pass
