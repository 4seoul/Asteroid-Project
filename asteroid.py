import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return "this was a small asteroid and we're done."

        log_event("asteroid_split")
        radius = self.radius
        rand = random.uniform(20, 50)
        mov1 = pygame.math.Vector2.rotate(self.velocity, rand)
        mov2 = pygame.math.Vector2.rotate(self.velocity, -rand)
        new_radius = radius - ASTEROID_MIN_RADIUS

        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

        new_asteroid_1.velocity = mov1 * 1.2
        new_asteroid_2.velocity = mov2 * 1.2

