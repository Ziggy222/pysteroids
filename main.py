# Allows use of open source pygame code
import pygame

# Allows use of Constants file for configuration management
from constants import * 

# Import Player support
from player import Player

# Import Asteroid support
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():

    # Initialize all pygame modules
    pygame.init()
    # Set up screen object with configured width and height
    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Establish main clock object and deltaTime variable
    mainGameClock = pygame.time.Clock()
    deltaTimeSeconds = 0

    # Set up object Groups for pygame
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Add Player to appropriate groups
    Player.containers = (updatable, drawable)

    # Set up Asteroid Groups
    Asteroid.containers = (asteroids, updatable, drawable)

    # Set up AsteroidField Group
    AsteroidField.containers = (updatable)
    
    # Intantiate Objects
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroidField = AsteroidField()

    # All rendering occurs here for clarity/clumping
    def render():
        # Fill screen with black
        screen.fill((0,0,0))
        
        # Draw all drawable objects
        for object in drawable:
            object.draw(screen)
        
        # Update display
        pygame.display.flip()
        # END RENDERING FUNCTIONS

    while(True):

        # Enable close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update all updatable game objects
        updatable.update(deltaTimeSeconds)
        
        # Render as final step before adjusting deltaTimeSeconds
        render()

        # Enforce 60f maximum for now, and store delta time
        deltaTimeSeconds = mainGameClock.tick(60)/1000.0

if __name__ == "__main__":
    main()
