import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

# Create sprite groups
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()  # <- STEP 3: Create the shots group

# Set static containers
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable,)
Shot.containers = (shots, updatable, drawable)  # <- STEP 3: Assign containers

# Create player and asteroid field instances
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
asteroid_field = AsteroidField()

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
           updatables.update(dt)
    for asteroid in asteroids:
        if asteroid.collides_with(player):
            print("Game over!")
            pygame.quit()
            exit()
            
    for asteroid in asteroids:
    for shot in shots:
        if asteroid.collides_with(shot):
            asteroid.kill()
            shot.kill()

        screen.fill("black")
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()
        
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
