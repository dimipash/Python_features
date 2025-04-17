"""
Demonstrates the use of lambda functions (anonymous functions) in Python.

Lambda functions are small, anonymous functions defined with the `lambda` keyword.
They can take any number of arguments but can only have one expression.
They are often used when a simple function is needed for a short period,
typically as an argument to higher-order functions like map(), filter(), sorted().
"""

if __name__ == "__main__":
    # Example 1: Simple lambda function to add two numbers
    add = lambda x, y: x + y
    print(f"Using lambda for addition: 5 + 3 = {add(5, 3)}")

    # Example 2: Using lambda with sorted() to sort a list of tuples by the second element
    points = [(1, 5), (3, 2), (8, 12), (5, 8)]
    points_sorted_by_y = sorted(points, key=lambda point: point[1])
    print(f"Original points: {points}")
    print(f"Points sorted by y-coordinate: {points_sorted_by_y}")

    # Example 3: Using lambda with filter() to get even numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Original numbers: {numbers}")
    print(f"Even numbers using filter and lambda: {even_numbers}")

    # Example 4: Using lambda with map() to square numbers
    squared_numbers = list(map(lambda x: x**2, numbers))
    print(f"Squared numbers using map and lambda: {squared_numbers}")
