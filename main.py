import sys
import pygame
from constants import (
    SCREEN_WIDTH, SCREEN_HEIGHT, 
    SCORE_PER_SECOND, SCORE_PER_ASTEROID
)
from player import Player
from asteroidfield import AsteroidField
from shot import Shot
from asteroid import Asteroid
from menu import main_menu, pause_screen, game_over_screen
from event_handler import handle_events

def main():
    """
    Main function to run the Asteroids game.
    Initializes pygame, sets up the game screen, and runs the game loop.
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    
    # Create font for score display
    score_font = pygame.font.Font(None, 36)  # None uses default font, 36 is the size

    # Display the main menu
    main_menu()
    
    # Main game loop that can be restarted
    while True:
        # Clear screen before starting a new game
        screen.fill("black")
        pygame.display.flip()
        
        # Setup new game
        dt = 0  # Delta time for frame rate independence
        clock = pygame.time.Clock()
        
        # Initialize score
        score = 0

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
                    print(f"Final Score: {int(score)}")
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
            
            # Add score for time survived
            score += SCORE_PER_SECOND * dt
                
            # Update game objects
            for game_object in updatable:
                game_object.update(dt)
            
            # Collision handling
            for asteroid in asteroids:
                if asteroid.collides_with(player):
                    # First clear everything to prevent the previous state from showing
                    screen.fill("black")
                    pygame.display.flip()
                    
                    # Empty all sprite groups to truly clear the game state
                    shots.empty()
                    asteroids.empty()
                    updatable.empty()
                    drawable.empty()
                    
                    # Show game over screen
                    if game_over_screen(screen, score) == "restart":
                        running = False  # Exit the inner game loop to restart
                    else:
                        # This should never happen as game_over_screen handles all options
                        pygame.quit()
                        sys.exit()
                    break  # Break collision loop after game over
                
                for shot in shots:
                    if asteroid.collides_with(shot):
                        # Add score for hitting asteroid
                        score += SCORE_PER_ASTEROID
                        asteroid.split()
                        shot.kill()

            # Draw game objects
            for game_object in drawable:
                game_object.draw(screen)
                
            # Draw HUD with score
            score_text = score_font.render(f"Score: {int(score)}", True, "white")
            screen.blit(score_text, (20, 20))  # Position in top-left corner with padding

            pygame.display.flip()  # Update display

            # Control frame rate
            dt = clock.tick(60) / 1000  # Convert ms to seconds

        # If we're here, either the player died and chose to restart,
        # or they quit the game (which would have already exited)

if __name__ == "__main__":
    main()