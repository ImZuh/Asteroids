import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, WHITE

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # Destroy this asteroid
        self.kill()

        # Too small to split
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Random split angle between 20 and 50 degrees
        angle = random.uniform(20, 50)

        # Calculate new velocity vectors
        vel1 = self.velocity.rotate(angle) * 1.2
        vel2 = self.velocity.rotate(-angle) * 1.2

        # New smaller radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Spawn two smaller asteroids at same position
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)

        # Assign new velocities
        a1.velocity = vel1
        a2.velocity = vel2
