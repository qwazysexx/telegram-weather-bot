class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("Abstract method")

    def describe(self):
        return f"This is a {self.name}."

class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius**2

rect = Rectangle("Rectangle", 5, 10)
circle = Circle("Circle", 7)

print(rect.describe())
print(f"Area of rectangle: {rect.area()}")  

print(circle.describe())
print(f"Area of circle: {circle.area()}")
