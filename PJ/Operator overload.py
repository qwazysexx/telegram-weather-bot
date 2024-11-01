import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __gt__(self, other):
        return self.length() > other.length()

    def __lt__(self, other):
        return self.length() < other.length()

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

v1 = Vector(3, 4)
v2 = Vector(1, 2)

v3 = v1 + v2
print(f'v1 + v2 = {v3}') 

v4 = v1 * 2
print(f'v1 * 2 = {v4}')  

print(f'v1 > v2: {v1 > v2}')  
print(f'v1 < v2: {v1 < v2}')  
