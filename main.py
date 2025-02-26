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

def initialize_game():
    """Initialize game objects and sprite groups"""
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
    
    return player, asteroidfield, shots, asteroids, updatable, drawable

def handle_collisions(player, shots, asteroids, score):
    """Handle collisions between game objects and return updated score"""
    for asteroid in asteroids:
        if asteroid.collides_with(player):
            return "game_over", score
            
        for shot in shots:
            if asteroid.collides_with(shot):
                # Add score for hitting asteroid
                score += SCORE_PER_ASTEROID
                asteroid.split()
                shot.kill()
    
    return None, score

def main():
    """
    Main function to run the Asteroids game.
    Initializes pygame, sets up the game screen, and runs the game loop.
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    
    # Create font for score display
    score_font = pygame.font.Font(None, 36)

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
        score = 0
        
        # Initialize game objects and sprite groups
        player, asteroidfield, shots, asteroids, updatable, drawable = initialize_game()

        # Game loop
        running = True
        paused = False
        
        while running:
            # Handle events first
            if not paused:
                event_result = handle_events(player, dt)
                if event_result == "pause":
                    paused = True
                    continue
                elif event_result == "quit":
                    running = False
                    print(f"Final Score: {int(score)}")
                    continue
            
            # Handle pause state
            if paused:
                screen.fill("black")
                if pause_screen(screen) == "resume":
                    paused = False
                dt = clock.tick(60) / 1000
                continue
                
            # Clear screen for game rendering
            screen.fill("black")
            
            # Add score for time survived
            score += SCORE_PER_SECOND * dt
                
            # Update game objects
            for game_object in updatable:
                game_object.update(dt)
            
            # Handle collisions
            result, score = handle_collisions(player, shots, asteroids, score)
            if result == "game_over":
                # Clear the screen and sprite groups
                screen.fill("black")
                pygame.display.flip()
                shots.empty()
                asteroids.empty()
                updatable.empty()
                drawable.empty()
                
                # Show game over screen
                if game_over_screen(screen, score) == "restart":
                    running = False  # Exit to restart
                else:
                    pygame.quit()
                    sys.exit()
                continue
                
            # Draw game objects
            for game_object in drawable:
                game_object.draw(screen)
                
            # Draw HUD with score
            score_text = score_font.render(f"Score: {int(score)}", True, "white")
            screen.blit(score_text, (20, 20))

            pygame.display.flip()
            dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()