# Allows use of open source pygame code
import pygame

# Allows use of Constants file for configuration management
from constants import * 

# Import Player support
from player import Player

# Import Asteroid support
from asteroidfield import AsteroidField
from asteroid import Asteroid

# Import shot support
from shot import Shot

def main():

    # Initialize all pygame modules
    pygame.init()
    # Set up screen object with configured width and height
    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Establish main clock object and deltaTime variable
    mainGameClock = pygame.time.Clock()
    deltaTimeSeconds = 0
    game_active = True

    # Set up object Groups for pygame
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Set up object groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
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

    while(game_active):
        # Enable close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update all updatable game objects
        updatable.update(deltaTimeSeconds)

        # Check asteroids collisions
        for asteroid in asteroids:
            if (asteroid.check_collision(player)):
                return
            for shot in shots:
                if (asteroid.check_collision(shot)):
                    shot.kill()
                    asteroid.split()
        
        # Render as final step before adjusting deltaTimeSeconds
        render()

        # Enforce 60f maximum for now, and store delta time
        deltaTimeSeconds = mainGameClock.tick(60)/1000.0

if __name__ == "__main__":
    main()
