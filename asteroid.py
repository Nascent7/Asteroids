import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

# slipts or kills asteroid based on radius compared to MIN radius from constants.py
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

 # generates random angle between 20-50 deg. and assignes it angle a and b
 # then calculates a new radius as  asteroid gets smaller       
        random_angle = random.uniform(20, 50)
        angle_a = self.velocity.rotate(random_angle)
        angle_b = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

# sets the position of the 2 new asrteoids as the same as where that old one was
# destroyed. calaculates new velocity with direction based off angle a and b
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = angle_a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = angle_b * 1.2
