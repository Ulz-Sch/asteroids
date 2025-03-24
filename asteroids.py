import pygame
import random

from constants import *
from circleshape import CircleShape

class Asteroid (CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white",self.position ,self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        a = self.velocity.rotate(angle)
        b = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        small_asteroid_1 = Asteroid(self.position.x,self.position.y , new_radius)
        small_asteroid_1.velocity = a * 1.2
        small_asteroid_2 = Asteroid(self.position.x,self.position.y , new_radius)
        small_asteroid_2.velocity = b * 1.2
