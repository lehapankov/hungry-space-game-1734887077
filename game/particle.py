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
        # Randomly choose between small and large particles
        self.size = random.choice([PARTICLE_SIZE_SMALL, PARTICLE_SIZE_LARGE])
        # Adjust velocity based on size - larger particles move slower
        velocity_factor = 1.5 if self.size == PARTICLE_SIZE_SMALL else 0.8
        self.velocity_x *= velocity_factor
        self.velocity_y *= velocity_factor
    
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
        # Create a mix of small and large particles
        # More small particles than large ones for better visual effect
        num_small = 8
        num_large = 4
        total_particles = num_small + num_large
        
        for _ in range(total_particles):
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
