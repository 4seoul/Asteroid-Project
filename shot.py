import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH) # drawing the bullets shot from the spaceship

    def update(self, dt):
        self.position += self.velocity * dt # updating it position 

