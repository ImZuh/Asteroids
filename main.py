import pygame
from constants import *

def main():
    pygame.init()  # Initialize pygame
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Quit if window closed
                
        screen.fill((0, 0, 0))  # Fill screen with black
        pygame.display.flip()   # Update the display

if __name__ == "__main__":
    main()
