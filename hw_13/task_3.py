from functools import wraps

'''3. Optional: Create a decorator that will check types.
It should take a function with arguments and validate inputs
with annotations. It should work for all possible functions.
Don`t forget to check the return type as well

Example:

@check_types
def add(a: int, b: int) -> int:
    return a + b

add(1, 2)
> 3

add("1", "2")
> TypeError: Argument a must be int, not str'''


def check_types(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Отримуємо анотації функції
        annotations = func.__annotations__

        # Перевіряємо типи аргументів
        for arg_name, arg_value in zip(annotations.keys(), args):
            expected_type = annotations[arg_name]
            if not isinstance(arg_value, expected_type):
                raise TypeError(f"Аргумент {arg_name} має бути типу "
                                f"{expected_type.__name__}, а не "
                                f"{type(arg_value).__name__}")

        # Викликаємо функцію та отримуємо результат
        result = func(*args, **kwargs)

        # Перевіряємо тип результату
        # Якщо анотація не вказана або відсутня,
        # то expected_return_type буде рівним None
        expected_return_type = annotations.get('return')
        if expected_return_type is not None and not isinstance(result, expected_return_type):
            raise TypeError(f"Повернене значення має бути типу"
                            f"{expected_return_type.__name__}, а не"
                            f"{type(result).__name__}")

        return result

    return wrapper


@check_types
def add(a: int, b: int) -> int:
    return a + b


''' {
    'a': int,
    'b': int,
    'return': int
}'''

try:
    add("1", "2")
except TypeError as error:
    print(error)


result = add(1, 2)

print(f'Результат = {result}')
