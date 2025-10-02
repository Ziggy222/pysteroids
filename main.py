# Allows use of open source pygame code
import pygame

# Allows use of Constants file for configuration management
from constants import * 

# Import Player support
from player import Player

def main():

    # Initialize all pygame modules
    pygame.init()
    # Set up screen object with configured width and height
    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Establish main clock object and deltaTime variable
    mainGameClock = pygame.time.Clock()
    deltaTimeSeconds = 0

    # Intantiate Player Object
    pc = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    while(True):

        # Enable close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        

        # Fill screen with black
        screen.fill((0,0,0))

        # Draw player
        pc.draw(screen)

        # Update display
        pygame.display.flip()

        # Enforce 60f maximum for now, and store delta time
        deltaTimeSeconds = mainGameClock.tick(60)/1000.0


if __name__ == "__main__":
    main()
