from vector import Vector
from color import *

import pygame
import physics
import math


class Ball:

    def __init__(self, surface):
        self.position = Vector(50, 50)
        self.size = 8
        self.color = white
        self.velocity = Vector(0, 0)
        self.max_power = 200
        self.boost = 8
        self.surface = surface
        self.pressed = False
        self.mouse_position = Vector()

    def get_position(self):
        return self.position

    def get_size(self):
        return self.size

    def get_velocity(self):
        return self.velocity

    def set_position(self, vector):
        self.position = vector

    def set_velocity(self, vector):
        self.velocity = vector

    def set_pressed(self, press):
        self.pressed = press

    def set_mouse_position(self, position):
        mouse_x, mouse_y = position
        self.mouse_position = Vector(mouse_x, mouse_y)

    def is_pressing(self):
        return self.pressed

    def is_moving(self):
        return self.velocity.get_coordinate() != Vector().get_coordinate()

    def calculate_trajectory(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_vector = Vector(mouse_x, mouse_y)

        angle = physics.angle(mouse_vector, self.mouse_position)
        power = physics.distance(self.mouse_position, mouse_vector)

        if power > self.max_power:
            power = self.max_power

        trajectory = physics.position(angle, power, self.position)

        return trajectory

    def calculate_velocity(self):
        trajectory = self.calculate_trajectory()
        vector = Vector(trajectory.get_x() - self.position.get_x(), trajectory.get_y() - self.position.get_y())
        vector.multiply(self.boost)
        return vector

    def render(self):
        pygame.draw.circle(self.surface, self.color, self.position.get_coordinate(), self.size)

        if self.is_pressing():
            trajectory = self.calculate_trajectory()
            pygame.draw.line(self.surface, red, self.position.get_coordinate(), trajectory.get_coordinate(), 3)

    def update(self, delta_time=1, minimum=1, decrease=0.98):
        x = self.velocity.get_x() * delta_time
        y = self.velocity.get_y() * delta_time

        self.position.add_x(x)
        self.position.add_y(y)

        if self.position.get_x() < self.size:
            self.velocity.negative_x()
            self.position.set_x(self.size)
        if self.position.get_x() > self.surface.get_width() - self.size:
            self.velocity.negative_x()
            self.position.set_x(self.surface.get_width() - self.size)
        if self.position.get_y() < self.size:
            self.velocity.negative_y()
            self.position.set_y(self.size)
        if self.position.get_y() > self.surface.get_height() - self.size:
            self.velocity.negative_y()
            self.position.set_y(self.surface.get_height() - self.size)

        distance = math.sqrt(self.velocity.get_x() ** 2 + self.velocity.get_y() ** 2)

        if distance > minimum:
            self.velocity.multiply(decrease)
        else:
            self.velocity = Vector()
