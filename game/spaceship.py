import pygame
from game.constants import *

class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size = 40
        self.update_surface()
        self.rect = self.image.get_rect()
        
        # Initialize movement variables
        self.velocity_x = 0
        self.velocity_y = 0
        self.speed_multiplier = SPACESHIP_BASE_SIZE / self.size
        
        # Initialize font for size display
        self.font = pygame.font.Font(None, int(self.size * 0.5))
    
    def update_surface(self):
        # Create a simple triangle shape for the spaceship
        self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        half_size = self.size // 2
        pygame.draw.polygon(self.image, WHITE, [
            (half_size, 0),
            (0, self.size),
            (self.size, self.size)
        ])
    
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.velocity_x = -SPACESHIP_SPEED * self.speed_multiplier
            elif event.key == pygame.K_RIGHT:
                self.velocity_x = SPACESHIP_SPEED * self.speed_multiplier
            elif event.key == pygame.K_UP:
                self.velocity_y = -SPACESHIP_SPEED * self.speed_multiplier
            elif event.key == pygame.K_DOWN:
                self.velocity_y = SPACESHIP_SPEED * self.speed_multiplier
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                self.velocity_x = 0
            elif event.key in (pygame.K_UP, pygame.K_DOWN):
                self.velocity_y = 0
    
    def update(self):
        # Update position
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
        
        # Keep spaceship within screen bounds
        self.rect.clamp_ip(pygame.display.get_surface().get_rect())
    
    def adjust_size(self, collected_size):
        # Grow slightly when collecting smaller items
        if collected_size < self.size:
            growth = collected_size * 0.1  # 10% of collected item's size
            self.size = min(100, self.size + growth)  # Cap at 100 pixels
            # Update speed multiplier based on new size
            self.speed_multiplier = SPACESHIP_BASE_SIZE / self.size
            # Update surface with new size
            self.update_surface()
            # Update rect position to maintain center
            old_center = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = old_center
    
    def draw(self, screen):
        # Draw the spaceship
        screen.blit(self.image, self.rect)
        
        # Draw size text
        size_text = self.font.render(str(int(self.size)), True, BLACK)
        text_rect = size_text.get_rect(center=(
            self.rect.centerx,
            self.rect.centery + self.size // 4
        ))
        screen.blit(size_text, text_rect)
