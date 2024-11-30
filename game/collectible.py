import pygame
import random
import math
from game.constants import *

class Collectible(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Randomly choose size with 70% small, 30% large probability
        self.size = COLLECTIBLE_SIZE_SMALL if random.random() < 0.7 else COLLECTIBLE_SIZE_LARGE
        self.points = POINTS_SMALL if self.size == COLLECTIBLE_SIZE_SMALL else POINTS_LARGE
        
        # Create surface based on size
        self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, WHITE, (self.size // 2, self.size // 2), self.size // 2)
        self.rect = self.image.get_rect()
        
        # Random starting position
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)
        
        # Random movement with random speed
        self.direction = random.uniform(0, 2 * math.pi)
        self.speed = random.uniform(COLLECTIBLE_SPEED_MIN, COLLECTIBLE_SPEED_MAX)
        self.velocity_x = math.cos(self.direction) * self.speed
        self.velocity_y = math.sin(self.direction) * self.speed
    
    def update(self):
        # Move collectible
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
        
        # Bounce off screen edges
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.velocity_x *= -1
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.velocity_y *= -1