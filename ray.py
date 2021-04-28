from vector import Vector


class RayInteractive:
    def intersection_point(self, ray):
        """Returns the intersection point of the object to with the ray"""
        pass

    def normal(self, intersection_point, ray):
        """Returns the normalized normal vector at the intersection point"""
        pass


class Ray:
    def __init__(self, origin, direction):
        self.origin = Vector(origin[0], origin[1])
        self.direction = Vector(direction[0], direction[1]).normalized()

    def __repr__(self):
        return f"Ray: {self.origin}, direction {self.direction}"

    def reflect(self, ray_interactive):
        """Checks if the ray intersects with the object,
        if it does this returns a new Ray, casted"""
        intersection_point = ray_interactive.intersection_point(self)

        if not intersection_point:
            return
        normal = ray_interactive.normal(intersection_point, self)
        reflection_direction = self.reflected_ray(normal)
        intersection = Vector(intersection_point[0], intersection_point[1])
        return Ray(intersection, reflection_direction)

    def reflected_ray(self, normal):
        """Returns the reflected ray direction based on the normal vector direction"""
        return self.direction - 2 * self.direction.dot(normal) * normal

    def is_in_direction(self, point):
        return (
                same_sign(point[0] - self.origin[0], self.direction[0])
                and same_sign(point[1] - self.origin[1], self.direction[1])
        )


def same_sign(x, y):
    if x == 0 and y == 0:
        return True
    elif (x == 0 and y != 0) or (x != 0 and y == 0):
        return False

    return x / abs(x) == y / abs(y)
