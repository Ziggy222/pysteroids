from constants import PLAYER_RADIUS, PLAYER_LINE_WIDTH
from constants import PLAYER_TURN_SPEED, PLAYER_MOVE_SPEED
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
        
    # Override parent's draw method to draw player triangle
    def draw(self, screen):
        pygame.draw.polygon(
            screen,
            "white",
            self.triangle(),
            PLAYER_LINE_WIDTH
        )

    # Support to rotate the player triangle 
    #  based upon deltaTime paramater - dt
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    # Modify player's position
    # Takes in deltaTime, in seconds, as dt
    def move(self, dt):
        # Create a unit vector in correct direction
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        # Apply Movement at appropriate speed and direction
        self.position += forward * PLAYER_MOVE_SPEED * dt        

    # Catch rotate key-pressed and respond.
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)