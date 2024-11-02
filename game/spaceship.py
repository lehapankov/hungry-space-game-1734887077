import pygame
from game.constants import *

class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Create a simple triangle shape for the spaceship
        self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, WHITE, [(20, 0), (0, 40), (40, 40)])
        self.rect = self.image.get_rect()
        
        # Starting position
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.centery = SCREEN_HEIGHT // 2
        
        # Movement
        self.velocity_x = 0
        self.velocity_y = 0
    
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.velocity_x = -SPACESHIP_SPEED
            elif event.key == pygame.K_RIGHT:
                self.velocity_x = SPACESHIP_SPEED
            elif event.key == pygame.K_UP:
                self.velocity_y = -SPACESHIP_SPEED
            elif event.key == pygame.K_DOWN:
                self.velocity_y = SPACESHIP_SPEED
        
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                self.velocity_x = 0
            elif event.key in (pygame.K_UP, pygame.K_DOWN):
                self.velocity_y = 0
    
    def update(self):
        # Update position
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
        
        # Keep spaceship in bounds
        self.rect.clamp_ip(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
