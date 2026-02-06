import pygame
from constants import LINE_WIDTH

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # initialising the cirlcle shapes
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen): # drawing itself
        surface = screen
        pygame.draw.circle(surface, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        position += (self.velocity * dt) # updating the position

    def collides_with(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius # checking if collision happens
