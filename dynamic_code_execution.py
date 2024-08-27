def demonstrate_exec():
    """
    Demonstrates the use of exec() to dynamically execute a string of Python code.
    Creates a function 'greet' and calls it with the argument "Alice".
    """
    code = """def greet(name):
    return f"Hello, {name}!\""""

    # Execute the code string
    local_scope = {}
    exec(code, {}, local_scope)
    print(local_scope["greet"]("Alice"))


def demonstrate_eval():
    """
    Demonstrates the use of eval() to evaluate a Python expression entered by the user.
    Prints the result of the evaluation.
    """
    # Evaluate the expression
    expression = input("Type an expression: ")

    result = eval(expression)

    print(f"Result of eval: {result}\n")


def demonstrate_safe_eval():
    """
    Demonstrates a safer use of eval() by providing a limited scope of variables.
    Evaluates an expression using predefined variables a, b, and c.
    """
    # Expression to evaluate
    expression = input("Type an expression that uses a, b and c: ")

    # Define variables for the expression
    variables = {"a": 2, "b": 3, "c": 4}

    # Evaluate the expression in the context of the provided variables
    result = eval(expression, {}, variables)

    print(f"Result of safe eval: {result}\n")


demonstrate_safe_eval()
