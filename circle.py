from vector import Vector
from line import Line
from ray import RayInteractive


class Circle(RayInteractive):
    def __init__(self, center, radius):
        self.r = radius
        self.center = Vector(center[0], center[1])

    def intersection_point(self, ray):
        line = Line(ray.origin, ray.origin + ray.direction * 11000)
        intersection = self.ray_intersection(ray)
        point = None

        # Secant line
        if intersection is not None:

            if type(intersection) == tuple:
                distance_origin_1 = (ray.origin - intersection[0]).magnitude()
                distance_origin_2 = (ray.origin - intersection[1]).magnitude()

                if distance_origin_1 < distance_origin_2:
                    point = intersection[0]

                else:
                    point = intersection[1]

            # Tangent line
            elif type(intersection) == Vector:
                point = intersection

        # Doesnt intersect
        if not point:
            return

        # If the intersection point direction from the origin is the same than the ray's direction
        if ray.is_in_direction(point):
            return point

    def ray_intersection(self, ray):

        # Y = mx + b
        if ray.direction.x == 0:
            m = 0
        else:
            m = ray.direction.y / ray.direction.x
        b = (ray.origin.y - self.center.y) - m * (ray.origin.x - self.center.x)

        determinant = (self.r * self.r) * (m * m) + self.r * self.r - b * b

        # Doesnt intersect
        if determinant < 0:
            return False

        # Tangent intersection
        elif determinant == 0:
            x = (-m * b) / (m * m + 1)
            return Vector(x, x * m + b + self.center.y)

        # Two intersections
        x1 = (-m * b + determinant ** 0.5) / (m * m + 1)
        x2 = (-m * b - determinant ** 0.5) / (m * m + 1)
        return (
            Vector(x1 + self.center.x, m * x1 + b + self.center.y),
            Vector(x2 + self.center.x, m * x2 + b + self.center.y)
        )

    def normal(self, intersection_point, ray):

        return intersection_point - self.center
