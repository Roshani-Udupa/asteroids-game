from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random

class Asteroid(CircleShape):
    score = 0
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, color="white", center=self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def collide(self, other):
        distance = pygame.math.Vector2.distance_to(self.position, other.position)
        return distance < (self.radius + other.radius)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            Asteroid.score += 10
            return
        Asteroid.score += 20
        rotate_angle = random.uniform(20,50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        vector1 = pygame.math.Vector2.rotate(self.velocity, rotate_angle)
        vector2 = pygame.math.Vector2.rotate(self.velocity, -rotate_angle)

        asteroid1.velocity = vector1*1.2
        asteroid2.velocity = vector2*1.2
        