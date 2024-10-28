def analyze_data(data):
    """
    Demonstrates pattern matching by analyzing different data structures.
    Handles dictionaries, lists, strings, and provides a default case.
    """
    match data:
        case {"type": "user", "name": str(name), "age": int(age)}:
            return f"User {name} is {age} years old"
        case ["error", message]:
            return f"Error occurred: {message}"
        case str(value):
            return f"Got string: {value}"
        case _:
            return "Unknown data format"


# Example usage
print(analyze_data({"type": "user", "name": "Alice", "age": 30}))
print(analyze_data(["error", "Connection failed"]))
print(analyze_data("Hello"))
