def demonstrate_walrus_operator():
    """
    Demonstrates the use of the walrus operator (:=) introduced in Python 3.8.
    The walrus operator allows assignment expressions, enabling assignment and
    return of a value in the same expression.
    """

    # Example 1: Using in while loop
    while (line := input("Enter something (or 'q' to quit): ")) != "q":
        print(f"You entered: {line}")

    # Example 2: Using in list comprehension
    numbers = [1, 2, 3, 4, 5]
    squares = [n_sq for x in numbers if (n_sq := x ** 2) > 10]
    print(f"Squares greater than 10: {squares}")

    # Example 3: Using in if statement
    if (length := len(numbers)) > 3:
        print(f"The list has {length} elements, which is more than 3")


if __name__ == "__main__":
    demonstrate_walrus_operator()
