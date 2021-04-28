class ReflectionsHandler:
    def __init__(self):
        self.obstacles = []
        self.reflection_rays = []

    def ray_casting(self, ray, rays_list, recursion_depth=0, max_recursion_depth=500):

        """
        The ray casting method uses linear algebra to calculate the
        intersection points of the ray and all it's reflected rays
        onto the lines. The algorithm is recursive, and the maximum
        level of recursion is determined by the max_recursion_depth parameter

        :param ray: The start ray to calculate ray casting
        :param rays_list: All the rays accumulated during the recursion
        :param recursion_depth: The level of recursion of the algorithm
        :return: List with all the rays
        """

        if recursion_depth > max_recursion_depth:
            return rays_list

        minimum_distance = float("inf")
        other_ray = None

        # Finds the closest ray intersection
        for obstacle in self.obstacles:
            intersection_ray = ray.reflect(obstacle)

            if not intersection_ray:
                continue

            distance = (ray.origin - intersection_ray.origin).magnitude()
            if distance < minimum_distance:
                other_ray = intersection_ray
                minimum_distance = distance

        # If a ray was casted onto another surface
        if other_ray:
            # Offset the ray along the normal direction to not check intersection twice
            other_ray.origin += other_ray.direction
            return self.ray_casting(
                ray=other_ray,
                rays_list=[other_ray] + rays_list,
                recursion_depth=recursion_depth + 1,
                max_recursion_depth=max_recursion_depth
            )

        else:
            return rays_list

    def update(self, source_ray, obstacles):
        self.obstacles = obstacles
        self.reflection_rays = self.ray_casting(source_ray, [source_ray])
