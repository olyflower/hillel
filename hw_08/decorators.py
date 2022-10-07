"""Створіть декоратор expected(), який перевіряє, чи те, що повертає декорована функція, має очікуваний тип."""

import functools


def expected(expected_types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(value):
            result = func(value)
            assert isinstance(result, expected_types), 'UnexpectedTypeError'
            return result
        return wrapper
    return decorator


@expected((str, int))
def print_value(value):
    print(value)
    return value


print_value("My text")
print_value(12324)
print_value([1, 4, 100])
