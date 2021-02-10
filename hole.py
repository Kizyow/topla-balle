from vector import Vector
from color import *
from random import *

import pygame
import physics


class Hole:

    def __init__(self, surface):
        self.position = Vector(surface.get_width() - 50, surface.get_height() - 50)
        self.size = 15
        self.color = black
        self.surface = surface

    def get_position(self):
        return self.position

    def get_size(self):
        return self.size

    def set_position(self, vector):
        self.position = vector

    def have_the_ball(self, vector):
        return physics.distance(self.position, vector) <= self.size

    def random_position(self):
        x = randint(self.size, self.surface.get_width() - self.size)
        y = randint(self.size, self.surface.get_height() - self.size)
        self.position = Vector(x, y)

    def render(self):
        pygame.draw.circle(self.surface, self.color, self.position.get_coordinate(), self.size)
