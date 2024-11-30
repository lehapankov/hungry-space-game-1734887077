import pygame
import random
import math
from game.constants import *

class Collectible(pygame.sprite.Sprite):
    def __init__(self, game=None, position=None, velocity=None):
        super().__init__()
        self.game = game
        # Generate random size between min and max using a more controlled distribution
        # Use round to prevent floating point precision issues
        self.size = round(random.uniform(COLLECTIBLE_SIZE_MIN, COLLECTIBLE_SIZE_MAX), 1)
        
        # Debug print to verify size distribution
        print(f"Created collectible with size: {self.size}")
        
        # Calculate points based on size
        self.points = int(5 + (self.size - COLLECTIBLE_SIZE_MIN) * 0.3)
        
        # Initialize font for size display - ensure minimum readable size
        font_size = max(12, int(self.size * 0.5))
        self.font = pygame.font.Font(None, font_size)
        
        # Create surface based on size using ceiling to ensure complete circle visibility
        size_int = math.ceil(self.size)
        self.image = pygame.Surface((size_int, size_int), pygame.SRCALPHA)
        # Draw circle with exact center and radius using float size
        center = size_int / 2
        pygame.draw.circle(self.image, WHITE, (center, center), self.size / 2)
        self.rect = self.image.get_rect()
        
        if position:
            self.rect.x, self.rect.y = position
        else:
            # Random starting position (now handled by Game class)
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)
        
        if velocity:
            self.velocity_x, self.velocity_y = velocity
        else:
            # Random movement with random speed
            self.direction = random.uniform(0, 2 * math.pi)
            self.speed = random.uniform(COLLECTIBLE_SPEED_MIN, COLLECTIBLE_SPEED_MAX)
            self.velocity_x = math.cos(self.direction) * self.speed
            self.velocity_y = math.sin(self.direction) * self.speed
    
    def update(self):
        # Move collectible
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
        
        # Kill if off screen
        if (self.rect.right < 0 or self.rect.left > SCREEN_WIDTH or 
            self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT):
            self.kill()
            
    def draw(self, screen):
        # Draw the collectible
        screen.blit(self.image, self.rect)
        
        # Render size text as whole number
        size_text = self.font.render(str(int(self.size)), True, BLACK)
        text_rect = size_text.get_rect(center=self.rect.center)
        screen.blit(size_text, text_rect)
