"""
Demonstrates the use of functools.partial in Python.

`functools.partial` allows you to "freeze" some portion of a function's arguments
and/or keywords, resulting in a new object with a simplified signature.
This is useful for creating specialized versions of existing functions.
"""

from functools import partial

def power(base, exponent):
    """Calculates the power of a base number."""
    return base ** exponent

def multiply(x, y):
    """Multiplies two numbers."""
    return x * y

if __name__ == "__main__":
    # Example 1: Creating a function that always squares a number
    square = partial(power, exponent=2)
    print(f"Using partial for squaring: square(5) = {square(5)}")
    print(f"Using partial for squaring: square(10) = {square(10)}")

    # Example 2: Creating a function that always cubes a number
    cube = partial(power, exponent=3)
    print(f"Using partial for cubing: cube(3) = {cube(3)}")

    # Example 3: Creating a function that always doubles a number using positional args
    double = partial(multiply, 2) # Freezes the first argument 'x' to 2
    print(f"Using partial for doubling: double(7) = {double(7)}")

    # Example 4: Freezing multiple arguments
    power_of_2 = partial(power, 2) # Freezes the base to 2
    print(f"Power of 2: 2^4 = {power_of_2(4)}")
    print(f"Power of 2: 2^8 = {power_of_2(8)}")

    # Example 5: Partial functions can also be used with methods or other callables
    # (More complex examples might involve classes or GUI callbacks)
