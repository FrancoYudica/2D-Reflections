
class Vector:
    """Simple vector class to allow easier vector operations"""
    def __init__(self, *args):
        if len(args) == 2:
            self.x = args[0]
            self.y = args[1]

        elif len(args) == 1 and len(args[0]) == 2:
            self.x, self.y = args[0]


    def __getitem__(self, item):
        if item == 0:
            return self.x
        return self.y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if type(other) == Vector:
            return self.dot(other)

        return Vector(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        return self.__mul__(1 / other)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def magnitude(self):
        return (self.x * self.x + self.y * self.y )**0.5

    def normalized(self):
        return self / self.magnitude()


""""
b = Vector(1, 1)
a = Vector(5, 6)
print(a + b)
print(a - b)
print(a * b)
print(a * 2)
print(a / 2)
print(b.normalized())
"""
