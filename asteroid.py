import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.immortal_time = 0
    
    def draw(self, screen):
        if self.immortal_time > 0:
            colour = "yellow"
        else:
            colour = "red"
        pygame.draw.circle(screen, colour, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        if self.immortal_time > 0:
            self.immortal_time -= dt

    def split(self):
        if self.immortal_time <= 0:
            self.kill()
            if self.radius <= ASTEROID_MIN_RADIUS:
                return
            angle = random.uniform(20, 50)
            positive_angle = self.velocity.rotate(angle)
            angle = random.uniform(20, 50)
            negative_angle = self.velocity.rotate(-angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS
            if new_radius < ASTEROID_MIN_RADIUS / 3:
                new_radius = ASTEROID_MIN_RADIUS / 3

            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = positive_angle * 1.2
            asteroid.immortal_time = 0.3
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = negative_angle *1.2
            asteroid.immortal_time = 0.3
        