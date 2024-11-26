import pygame
import sys
from game.spaceship import Spaceship
from game.collectible import Collectible
from game.particle import ParticleSystem
from game.constants import *

class Game:
    def __init__(self):
        print("Initializing game...")
        try:
            pygame.init()
            print("Pygame initialized successfully")
            
            pygame.mixer.init()
            print("Pygame mixer initialized successfully")
            
            self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
            pygame.display.set_caption("Hungry Space")
            print("Display window created successfully")
            
            # Load sounds with error handling
            try:
                self.collect_sound = pygame.mixer.Sound('assets/sounds/collect.wav')
                self.gameover_sound = pygame.mixer.Sound('assets/sounds/gameover.wav')
                print("Sound files loaded successfully")
            except Exception as e:
                print(f"Warning: Could not load sound files: {e}")
                # Create dummy sound object that does nothing when played
                class DummySound:
                    def play(self): pass
                self.collect_sound = self.gameover_sound = DummySound()
            
            # Create game objects
            self.spaceship = Spaceship()
            self.collectibles = pygame.sprite.Group()
            self.particle_system = ParticleSystem()
            print("Game objects created successfully")
            
            # Game state
            self.score = 0
            self.font = pygame.font.Font(None, 36)
            self.clock = pygame.time.Clock()
            
            # Spawn initial collectibles
            self.spawn_collectibles(5)
            print("Initial setup complete")
            
        except Exception as e:
            print(f"Fatal error during game initialization: {e}")
            pygame.quit()
            sys.exit(1)
        
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
            self.score += collision.points
            self.collect_sound.play()
            self.particle_system.create_particles(collision.rect.center)
            self.spawn_collectibles(1)  # Spawn new collectible
            
    def draw(self):
        try:
            self.screen.fill(BACKGROUND_COLOR)
            print(f"Screen cleared with background color: {BACKGROUND_COLOR}")
            
            # Draw game objects
            self.collectibles.draw(self.screen)
            self.spaceship.draw(self.screen)
            self.particle_system.draw(self.screen)
            
            # Draw score
            score_text = self.font.render(f'Score: {self.score}', True, WHITE)
            self.screen.blit(score_text, (10, 10))
            
            pygame.display.flip()
            print("Frame rendered successfully")
        except Exception as e:
            print(f"Error during drawing: {e}")
    
    def run(self):
        print("Starting game loop...")
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
