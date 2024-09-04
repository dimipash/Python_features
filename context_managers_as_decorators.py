"""
This code demonstrates the use of context managers and decorators in Python.
Context managers are used to manage resources, such as opening and closing files, and can be used as decorators.
Decorators are used to modify the behavior of a function without changing its code.
In this example, the timer and suppress_exceptions context managers are used to measure and suppress exceptions.
The timer_decorator and exception_handler decorators are used to measure and handle exceptions in functions.
"""

import time
from contextlib import contextmanager


@contextmanager
def timer():
    """A context manager that measures execution time."""
    start_time = time.time()
    try:
        yield
    finally:
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.4f} seconds")


@contextmanager
def suppress_exceptions(*exception_types):
    """A context manager that suppresses specified exceptions."""
    try:
        yield
    except exception_types as e:
        print(f"Suppressed exception: {type(e).__name__}: {e}")


def timer_decorator(func):
    """A decorator that measures and prints the execution time of a function."""

    def wrapper(*args, **kwargs):
        with timer():
            return func(*args, **kwargs)

    return wrapper


def exception_handler(func):
    """A decorator that handles exceptions in a function."""

    def wrapper(*args, **kwargs):
        with suppress_exceptions(ValueError, ZeroDivisionError):
            return func(*args, **kwargs)

    return wrapper


@timer_decorator
def slow_function():
    """A function that simulates a time-consuming operation."""
    time.sleep(2)
    print("Slow operation completed")


@exception_handler
def risky_function(x):
    """A function that might raise exceptions."""
    if x == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    elif x < 0:
        raise ValueError("x must be non-negative")
    else:
        return 10 / x


if __name__ == "__main__":
    print("Using context managers directly:")
    with timer():
        time.sleep(1)
        print("Operation inside timer context")

    with suppress_exceptions(ValueError, ZeroDivisionError):
        1 / 0

    print("\nUsing context managers as decorators:")
    slow_function()

    print("\nTesting exception handler:")
    for x in [2, 0, -1]:
        result = risky_function(x)
        print(f"Result for x={x}: {result}")

    print("\nUsing multiple context managers:")
    with timer(), suppress_exceptions(ValueError, ZeroDivisionError):
        time.sleep(0.5)
        1 / 0
        print("This line won't be reached")
