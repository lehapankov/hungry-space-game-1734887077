import pygame
import random
from game.constants import *

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity_x = random.uniform(-2, 2)
        self.velocity_y = random.uniform(-2, 2)
        self.lifetime = PARTICLE_LIFETIME
        self.color = random.choice(PARTICLE_COLORS)
        self.size = random.randint(2, 4)
    
    def update(self):
        self.x += self.velocity_x
        self.y += self.velocity_y
        self.lifetime -= 1
    
    def is_alive(self):
        return self.lifetime > 0

class ParticleSystem:
    def __init__(self):
        self.particles = []
    
    def create_particles(self, position):
        for _ in range(10):
            self.particles.append(Particle(*position))
    
    def update(self):
        self.particles = [p for p in self.particles if p.is_alive()]
        for particle in self.particles:
            particle.update()
    
    def draw(self, screen):
        for particle in self.particles:
            pygame.draw.circle(screen, particle.color,
                             (int(particle.x), int(particle.y)),
                             particle.size)
