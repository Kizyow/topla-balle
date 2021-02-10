import pygame

from color import *

from ball import Ball
from hole import Hole


class Game:

    def __init__(self, name, width, height, framerate=60):
        self.name = name
        self.width = width
        self.height = height
        self.framerate = framerate

        pygame.init()
        pygame.display.set_caption(name)

        self.surface = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.running = False

        self.ball = Ball(self.surface)
        self.hole = Hole(self.surface)

        self.score = 0

    def launch(self):
        self.running = True

        while self.running:
            delta_time_ms = self.clock.tick(self.framerate)
            delta_time = delta_time_ms / 1000

            self.game_event()
            self.check_ball_is_in_hole()
            self.render()
            self.ball.update(delta_time)

    def stop(self):
        self.running = False
        pygame.quit()

    def game_event(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stop()

            if not self.ball.is_moving():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        mouse = pygame.mouse.get_pos()
                        self.ball.set_mouse_position(mouse)
                        self.ball.set_pressed(True)

                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == pygame.BUTTON_LEFT:
                        vector = self.ball.calculate_velocity()
                        self.ball.set_velocity(vector)
                        self.ball.set_pressed(False)

    def check_ball_is_in_hole(self):
        if self.hole.have_the_ball(self.ball.position):
            self.hole.random_position()
            self.score += 1

    def score_text(self):
        font = pygame.font.SysFont('Comic Sans MS', 32)
        text = font.render("Score: " + str(self.score), False, white)
        self.surface.blit(text, (self.surface.get_width() / 2 - 80, 20))

    def render(self):
        self.surface.fill(green)
        self.hole.render()
        self.ball.render()
        self.score_text()
        pygame.display.flip()
