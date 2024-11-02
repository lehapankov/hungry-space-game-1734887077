import pygame
import sys
from game.spaceship import Spaceship
from game.collectible import Collectible
from game.particle import ParticleSystem
from game.constants import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Hungry Space")
        
        # Load sounds
        self.collect_sound = pygame.mixer.Sound('assets/sounds/collect.wav')
        self.gameover_sound = pygame.mixer.Sound('assets/sounds/gameover.wav')
        
        # Create game objects
        self.spaceship = Spaceship()
        self.collectibles = pygame.sprite.Group()
        self.particle_system = ParticleSystem()
        
        # Game state
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.clock = pygame.time.Clock()
        
        # Spawn initial collectibles
        self.spawn_collectibles(5)
        
    def spawn_collectibles(self, count):
        for _ in range(count):
            self.collectibles.add(Collectible())
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            self.spaceship.handle_event(event)
        return True
    
    def update(self):
        self.spaceship.update()
        self.collectibles.update()
        self.particle_system.update()
        
        # Check collisions
        collisions = pygame.sprite.spritecollide(self.spaceship, self.collectibles, True)
        for collision in collisions:
            self.score += 10
            self.collect_sound.play()
            self.particle_system.create_particles(collision.rect.center)
            self.spawn_collectibles(1)  # Spawn new collectible
            
    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        
        # Draw game objects
        self.collectibles.draw(self.screen)
        self.spaceship.draw(self.screen)
        self.particle_system.draw(self.screen)
        
        # Draw score
        score_text = self.font.render(f'Score: {self.score}', True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        pygame.display.flip()
    
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    game = Game()
    game.run()
