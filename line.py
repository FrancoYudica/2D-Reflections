from vector import Vector
from ray import RayInteractive


class Line(RayInteractive):
    def __init__(self, point1, point2):
        self.p1 = Vector(point1[0], point1[1])
        self.p2 = Vector(point2[0], point2[1])

    def line_intersect(self, other):
        """ returns a (x, y) tuple or None if there is no intersection """
        d = (other.p2.y - other.p1.y) * (self.p2.x - self.p1.x) - (other.p2.x - other.p1.x) * (self.p2.y - self.p1.y)
        if d:
            uA = ((other.p2.x - other.p1.x) * (self.p1.y - other.p1.y) - (other.p2.y - other.p1.y) * (
                    self.p1.x - other.p1.x)) / d
            uB = ((self.p2.x - self.p1.x) * (self.p1.y - other.p1.y) - (self.p2.y - self.p1.y) * (
                    self.p1.x - other.p1.x)) / d
        else:
            return
        if not (0 <= uA <= 1 and 0 <= uB <= 1):
            return
        x = self.p1.x + uA * (self.p2.x - self.p1.x)
        y = self.p1.y + uA * (self.p2.y - self.p1.y)
        return x, y

    def intersection_point(self, ray):
        return self.line_intersect(Line(ray.origin, ray.origin + ray.direction * 1000000))

    def normal(self, intersection_point, ray):
        return Vector(-(self.p1.y - self.p2.y), (self.p1.x - self.p2.x)).normalized()
