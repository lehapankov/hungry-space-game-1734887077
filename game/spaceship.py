import pygame
from game.constants import *

class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size = 40
        self.update_surface()
        self.rect = self.image.get_rect()
        
        # Center the spaceship at start
        screen = pygame.display.get_surface()
        self.rect.center = (screen.get_width() // 2, screen.get_height() // 2)
        
        # Initialize movement variables
        self.velocity_x = 0
        self.velocity_y = 0
        self.speed_multiplier = SPACESHIP_BASE_SIZE / self.size
        
        # Physics variables for inertia
        self.acceleration = 0.5
        self.friction = 0.98
        self.max_speed = SPACESHIP_SPEED
        
        # Key state tracking
        self.keys_pressed = {
            pygame.K_LEFT: False,
            pygame.K_RIGHT: False,
            pygame.K_UP: False,
            pygame.K_DOWN: False
        }
        
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
            if event.key in self.keys_pressed:
                self.keys_pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            if event.key in self.keys_pressed:
                self.keys_pressed[event.key] = False
    
    def update(self):
        # Handle continuous acceleration based on key states
        if self.keys_pressed[pygame.K_LEFT]:
            self.velocity_x -= self.acceleration * self.speed_multiplier
        if self.keys_pressed[pygame.K_RIGHT]:
            self.velocity_x += self.acceleration * self.speed_multiplier
        if self.keys_pressed[pygame.K_UP]:
            self.velocity_y -= self.acceleration * self.speed_multiplier
        if self.keys_pressed[pygame.K_DOWN]:
            self.velocity_y += self.acceleration * self.speed_multiplier

        # Apply friction
        self.velocity_x *= self.friction
        self.velocity_y *= self.friction
        
        # Clamp velocities to max_speed
        max_vel = self.max_speed * self.speed_multiplier
        self.velocity_x = max(min(self.velocity_x, max_vel), -max_vel)
        self.velocity_y = max(min(self.velocity_y, max_vel), -max_vel)
        
        # Update position
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
        
        # Keep spaceship within screen bounds
        self.rect.clamp_ip(pygame.display.get_surface().get_rect())
    
    def adjust_size(self, collected_size):
        # Grow slightly when collecting smaller items
        if collected_size < self.size:
            growth = collected_size * 0.1  # 10% of collected item's size
            self.size = min(100.0, self.size + growth)  # Cap at exactly 100.0 pixels
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
