from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random
import math

class Asteroid(CircleShape):
    score = 0
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        points = []
        for i in range(10):  # number of "edges" -> more = smoother asteroid
            angle = i * (2 * math.pi / 10)
            r = self.radius + random.randint(-5, 5)  # randomize shape
            x = self.position[0] + r * math.cos(angle)
            y = self.position[1] + r * math.sin(angle)
            points.append((x, y))

        pygame.draw.polygon(screen, (255, 255, 255), points, width=2)

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
        