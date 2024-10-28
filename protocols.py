from typing import Protocol, runtime_checkable

@runtime_checkable
class Drawable(Protocol):
    """Protocol defining objects that can be drawn via a draw() method."""

    def draw(self) -> str: ...


class Circle:
    """Implements Drawable protocol with circle-specific drawing."""

    def draw(self) -> str:
        return "Drawing a circle"

class Square:
    def draw(self) -> str:
        return "Drawing a square"

def render(shape: Drawable) -> None:
    """Renders any shape that implements the Drawable protocol."""
    print(shape.draw())


# Usage
circle = Circle()
square = Square()
render(circle)
render(square)
