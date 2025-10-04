from circleshape import CircleShape

from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS, ASTEROID_SPEED_UP_AFTER_BREAK
from constants import ASTEROID_BREAK_MIN_ANGLE, ASTEROID_BREAK_MAX_ANGLE

import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen,"white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if (self.radius <= ASTEROID_MIN_RADIUS):
            return
        angle = random.uniform(ASTEROID_BREAK_MIN_ANGLE,ASTEROID_BREAK_MAX_ANGLE)
        vel1 = self.velocity.rotate(angle)
        vel2 = self.velocity.rotate(-angle)
        newRadius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position[0], self.position[1], newRadius)
        asteroid2 = Asteroid(self.position[0], self.position[1], newRadius)
        asteroid1.velocity = vel1 * ASTEROID_SPEED_UP_AFTER_BREAK
        asteroid2.velocity = vel2 * ASTEROID_SPEED_UP_AFTER_BREAK