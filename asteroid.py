import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH) # Drawing the asteroid 

    def update(self, dt):
        self.position += self.velocity * dt # Moving the asteroid

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return "this was a small asteroid and we're done." # If its size is too small it deletes itself

        log_event("asteroid_split") # splits the asteroid into 2 smaller asteroids
        radius = self.radius
        rand = random.uniform(20, 50)
        mov1 = pygame.math.Vector2.rotate(self.velocity, rand)
        mov2 = pygame.math.Vector2.rotate(self.velocity, -rand)
        new_radius = radius - ASTEROID_MIN_RADIUS

        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius) # initialising the new smaller asteroids
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

        new_asteroid_1.velocity = mov1 * 1.2 # setting the velocity of the new asteroids
        new_asteroid_2.velocity = mov2 * 1.2

