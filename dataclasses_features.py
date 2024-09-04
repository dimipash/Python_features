"""
This code demonstrates the use of dataclasses in Python.
Dataclasses are a feature in Python that provide a convenient way to create classes with default methods.
In this example, the Person and Employee classes are dataclasses that have a name, age, email, and address.
The Employee class also has a job_title, salary, and skills.
"""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Person:
    name: str
    age: int
    email: str
    address: Optional[str] = None

    def greet(self) -> str:
        return f"Hello, my name is {self.name} and I'm {self.age} years old."


@dataclass
class Employee(Person):
    job_title: str
    salary: float
    skills: List[str] = field(default_factory=list)

    def __post_init__(self):
        if self.salary < 0:
            raise ValueError("Salary cannot be negative")

    def annual_salary(self) -> float:
        return self.salary * 12


@dataclass(frozen=True)
class ImmutablePoint:
    x: float
    y: float


if __name__ == "__main__":
    # Creating a Person instance
    person = Person("Alice", 30, "alice@example.com")
    print(person)
    print(person.greet())

    # Creating an Employee instance
    employee = Employee(
        "Bob",
        35,
        "bob@example.com",
        "123 Main St",
        "Developer",
        5000,
        ["Python", "JavaScript"],
    )
    print(employee)
    print(f"Annual salary: ${employee.annual_salary():.2f}")

    # Demonstrating default values and factory functions
    another_employee = Employee(
        "Charlie", 40, "charlie@example.com", job_title="Manager", salary=6000
    )
    print(another_employee)

    # Demonstrating immutability
    point = ImmutablePoint(1.0, 2.0)
    print(point)
    try:
        point.x = 3.0  # This will raise an error
    except AttributeError as e:
        print(f"Error: {e}")

    # Demonstrating equality comparison
    person1 = Person("David", 25, "david@example.com")
    person2 = Person("David", 25, "david@example.com")
    print(f"person1 == person2: {person1 == person2}")
