import pygame

# Base class for game objects in Pysteroids.
# Inherits Sprite from pygame and uses a point-radius structure
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # 10/1/2025 - I don't know what this is doing yet
        # It is being included because it's part of the initial
        # tutorial and will be explained and used later.
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        # Build a position Vector based on the passed values
        self.position = pygame.Vector2(x, y)
        # Give self a velocity of 0,0 for now
        self.velocity = pygame.Vector2(0,0)
        # Set radius to passed value
        self.radius = radius

    # Sub-classes must override the following methods
    def draw(self, screen):
        pass

    def update(self, dt):
        pass