import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Create sprite groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Set static containers
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables,)
    Shot.containers = (shots, updatables, drawables)

    # Create player and asteroid field instances
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, updatables, drawables)  # <-- Added sprite groups here
    asteroid_field = AsteroidField()

    # Game loop
    running = True
    while running:
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        updatables.update(dt)

        # Check collision: player with asteroid
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                pygame.quit()
                return

        # Check collision: shot with asteroid
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    asteroid.kill()
                    shot.kill()

        screen.fill("black")
        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
