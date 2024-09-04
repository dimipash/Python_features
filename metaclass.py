"""
This code demonstrates the use of a metaclass in Python.
A metaclass is a class that defines how a class behaves.
In this example, the Meta class is a metaclass that converts all method names to uppercase.
"""


class Meta(type):
    def __new__(cls, name, bases, attrs):
        # Convert all method names to uppercase
        uppercase_attrs = {
            key.upper(): value
            for key, value in attrs.items()
            if not key.startswith("__")
        }
        return super().__new__(cls, name, bases, {**attrs, **uppercase_attrs})


class MyClass(metaclass=Meta):
    def hello(self):
        return "Hello, World!"


if __name__ == "__main__":
    obj = MyClass()
    print(obj.HELLO())  # Output: Hello, World!
    print(obj.hello())  # This also works, output: Hello, World!

    # Demonstrating that the original method name still exists
    print(hasattr(obj, "hello"))  # Output: True
    print(hasattr(obj, "HELLO"))  # Output: True
