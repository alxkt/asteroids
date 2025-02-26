import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroidfield import AsteroidField
from shot import Shot
from asteroid import Asteroid
from menu import main_menu

def main():
    """
    Main function to run the Asteroids game.
    Initializes pygame, sets up the game screen, and runs the game loop.
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    # Display the main menu
    main_menu()

    dt = 0  # Delta time for frame rate independence
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 74)

    # Sprite groups for different game objects
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Assign sprite containers
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    # Initialize game objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    # Game loop
    running = True
    paused = False
    
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = not paused  # Toggle pause state
                elif event.key == pygame.K_SPACE and not paused:
                    player.shoot()
        
        # Clear screen
        screen.fill("black")
        
        # If paused, draw pause screen and skip game updates
        if paused:
            pause_text = font.render("PAUSED", True, "white")
            resume_text = font.render("Press ESC to Resume", True, "white")
            quit_text = font.render("Press Q to Quit", True, "white")

            screen.blit(pause_text, (SCREEN_WIDTH // 2 - pause_text.get_width() // 2, SCREEN_HEIGHT // 4))
            screen.blit(resume_text, (SCREEN_WIDTH // 2 - resume_text.get_width() // 2, SCREEN_HEIGHT // 2))
            screen.blit(quit_text, (SCREEN_WIDTH // 2 - quit_text.get_width() // 2, SCREEN_HEIGHT // 2 + 100))
            
            # Check for quit during pause
            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]:
                running = False
        else:
            # Only process game updates when not paused
            
            # Get keyboard state for continuous movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                player.rotate(-dt)
            if keys[pygame.K_d]:
                player.rotate(dt)
            if keys[pygame.K_w]:
                player.move(dt)
            if keys[pygame.K_s]:
                player.move(-dt)

            # Update game objects
            for object in updatable:
                object.update(dt)
            
            # Collision handling
            for asteroid in asteroids:
                if asteroid.collides_with(player):
                    print("Game over!")
                    pygame.quit()
                    sys.exit()
                for shot in shots:
                    if asteroid.collides_with(shot):
                        asteroid.split()
                        shot.kill()

            # Draw game objects
            for object in drawable:
                object.draw(screen)

        pygame.display.flip()  # Update display

        # Control frame rate
        dt = clock.tick(60) / 1000  # Convert ms to seconds

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()