from random import randint

import pygame

from vector import Vector
from circle import Circle
from line import Line
from ray import Ray
from relfections_handler import ReflectionsHandler
import math


def positive_sin(x):
    return (math.sin(x) + 1) * 0.5


def _rainbow_color(step):
    return int(255 * positive_sin(step)), int(255 * positive_sin(step + 2)), int(255 * positive_sin(step + 4))


class Program:
    def __init__(self, display_size):
        self.display_size = Vector(display_size)
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((display_size[0], display_size[1]), pygame.SCALED | pygame.RESIZABLE)

        self.ray = Ray(Vector(100, 200), Vector(1, -1))

        self.obstacles = [
            Circle(
                (randint(0, self.display_size[0]), randint(0, self.display_size[1])),
                randint(10, self.display_size[0] / 5)
            )
            for _ in range(10)
        ]

        self.start_line_pos = None
        self.reflections_handler = ReflectionsHandler()

    def loop(self):
        running = True

        while running:
            dt = self.clock.tick(100) / 1000 * 60

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                else:
                    self.event(event)

            mouse = Vector(pygame.mouse.get_pos())
            self.update(dt, mouse)
            self.draw(self.display)
            pygame.display.flip()

        pygame.quit()
        quit()

    def event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == pygame.BUTTON_LEFT:

                if not self.start_line_pos:
                    self.start_line_pos = event.pos
                    self.obstacles.append(Line(self.start_line_pos, event.pos))

                else:
                    self.start_line_pos = None

            elif event.button == pygame.BUTTON_RIGHT:
                self.ray.origin = Vector(event.pos[0], event.pos[1])

        elif event.type == pygame.MOUSEWHEEL:
            self.ray.direction.rotate(event.y * 0.1)

    def update(self, dt: float, mouse: Vector):

        origin_mouse = (mouse - self.ray.origin)

        if origin_mouse.magnitude() > 0:
            self.ray.direction = origin_mouse.normalized()

        if self.start_line_pos:
            self.obstacles[-1].p1 = Vector(mouse[0], mouse[1])
        self.reflections_handler.update(self.ray, self.obstacles)

    def draw(self, surface: pygame.Surface):
        surface.fill((0, 0, 0))

        self.draw_rays(surface, _rainbow_color(pygame.time.get_ticks() / 300))

        for obstacle in self.obstacles:
            if isinstance(obstacle, Circle):
                pygame.draw.circle(
                    surface,
                    (255, 255, 255),
                    (int(obstacle.center.x), int(obstacle.center.y)),
                    obstacle.r, 2
                )

            elif isinstance(obstacle, Line):
                pygame.draw.line(
                    surface,
                    (255, 255, 255),
                    (int(obstacle.p1.x), int(obstacle.p1.y)),
                    (int(obstacle.p2.x), int(obstacle.p2.y)),
                    2
                )

    def draw_rays(self, surface, color, thickness=4):
        rays = self.reflections_handler.reflection_rays
        end = rays[0].origin + rays[0].direction * 1999

        pygame.draw.line(
            surface,
            color,
            (int(rays[0].origin.x), int(rays[0].origin.y)),
            (int(end.x), int(end.y)),
            thickness
        )
        for i in range(len(rays) - 1):
            pygame.draw.line(
                surface,
                color,
                (int(rays[i].origin.x), int(rays[i].origin.y)),
                (int(rays[i + 1].origin.x), int(rays[i + 1].origin.y)),
                thickness
            )
