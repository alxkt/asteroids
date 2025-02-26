import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroidfield import AsteroidField
from shot import Shot
from asteroid import Asteroid
from menu import main_menu, pause_screen
from event_handler import handle_events

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

    # Sprite groups for different game objects
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Assign sprite containers
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    # Initialize game objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    # Game loop
    running = True
    paused = False
    
    while running:
        # Handle events first
        if not paused:
            event_result = handle_events(player, dt)
            if event_result == "pause":
                paused = True
                # Skip to pause screen immediately without updating the game
                continue
            elif event_result == "quit":
                running = False
                continue
        
        # Handle pause state
        if paused:
            # Clear screen before showing pause screen
            screen.fill("black")
            # Use the pause screen from menu.py
            if pause_screen(screen) == "resume":
                paused = False
            # Skip the rest of the game update when paused
            dt = clock.tick(60) / 1000  # Still need to control frame rate
            continue
            
        # Clear screen for game rendering
        screen.fill("black")
            
        # Update game objects
        for game_object in updatable:
            game_object.update(dt)
        
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
        for game_object in drawable:
            game_object.draw(screen)

        pygame.display.flip()  # Update display

        # Control frame rate
        dt = clock.tick(60) / 1000  # Convert ms to seconds

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()