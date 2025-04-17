"""
Demonstrates the use of list comprehensions in Python.

List comprehensions provide a concise way to create lists.
Common applications are to make new lists where each element is the result of some
operations applied to each member of another sequence or iterable, or to create a
subsequence of those elements that satisfy a certain condition.
"""

if __name__ == "__main__":
    # Example 1: Simple list comprehension to create squares of numbers
    numbers = [1, 2, 3, 4, 5]
    squares = [n**2 for n in numbers]
    print(f"Original numbers: {numbers}")
    print(f"Squares (using list comprehension): {squares}")

    # Example 2: List comprehension with a condition (even numbers)
    even_numbers = [n for n in numbers if n % 2 == 0]
    print(f"Even numbers from the list: {even_numbers}")

    # Example 3: List comprehension with a transformation and condition
    squared_odds = [n**2 for n in numbers if n % 2 != 0]
    print(f"Squares of odd numbers: {squared_odds}")

    # Example 4: Creating a list of tuples
    pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
    print(f"List of pairs: {pairs}")
