def demonstrate_structural_pattern_matching():
    """
    Demonstrates structural pattern matching introduced in Python 3.10.
    This feature provides a more powerful and expressive way to handle
    conditional logic compared to traditional if-elif-else statements.
    """

    def process_data(data):
        match data:
            case {"type": "user", "name": name, "age": age}:
                return f"User {name}, age {age}"
            case {"type": "product", "name": name, "price": price}:
                return f"Product {name}, price ${price:.2f}"
            case [first, *rest]:
                return f"List with first element {first} and {len(rest)} more"
            case str() as text if len(text) > 10:
                return f"Long text: {text[:10]}..."
            case str() as text:
                return f"Short text: {text}"
            case _:
                return "Unknown data type"

    # Example 1: Matching dictionaries
    user_data = {"type": "user", "name": "Alice", "age": 30}
    print(process_data(user_data))

    # Example 2: Matching lists
    numbers = [1, 2, 3, 4, 5]
    print(process_data(numbers))

    # Example 3: Matching strings
    long_text = "This is a very long string"
    print(process_data(long_text))

    # Example 4: Default case
    unknown_data = 3.14
    print(process_data(unknown_data))


if __name__ == "__main__":
    demonstrate_structural_pattern_matching()
