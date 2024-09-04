"""
This code demonstrates the use of property decorators in Python.
A property decorator allows you to define a method that can be accessed like an attribute.
In this example, the Temperature class has two properties: celsius and fahrenheit.
The celsius property has a setter that validates the input to ensure it is not below absolute zero.
"""


class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        """Get the current temperature in Celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Set the temperature in Celsius."""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible.")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Get the current temperature in Fahrenheit."""
        return (self.celsius * 9 / 5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set the temperature in Fahrenheit."""
        self.celsius = (value - 32) * 5 / 9


if __name__ == "__main__":
    temp = Temperature()

    # Using the celsius property
    temp.celsius = 25
    print(f"Temperature in Celsius: {temp.celsius}°C")
    print(f"Temperature in Fahrenheit: {temp.fahrenheit}°F")

    # Using the fahrenheit property
    temp.fahrenheit = 98.6
    print(f"Temperature in Celsius: {temp.celsius:.2f}°C")
    print(f"Temperature in Fahrenheit: {temp.fahrenheit}°F")

    # Demonstrating value validation
    try:
        temp.celsius = -300
    except ValueError as e:
        print(f"Error: {e}")
