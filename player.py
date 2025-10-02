from constants import PLAYER_RADIUS, PLAYER_LINE_WIDTH
import pygame

from circleshape import CircleShape

class Player(CircleShape):

    def __init__(self, x, y):
        # Call Parent constructor
        super().__init__(x, y, PLAYER_RADIUS)
        # Set default rotation to 0
        self.rotation = 0

    # Define the points of the displayable triangle
    def triangle(self):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        right = (
            pygame.Vector2(0,1).rotate(self.rotation + 90) 
            * self.radius / 1.5
            )
        # Build the three points based upon direction vectors
        # And radius
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right

        return [a,b,c]
        
    def draw(self, screen):
        pygame.draw.polygon(
            screen,
            "white",
            self.triangle(),
            PLAYER_LINE_WIDTH
        )