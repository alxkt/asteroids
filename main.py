import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroidfield import AsteroidField
from shot import Shot
from asteroid import Asteroid

def main():
    """
    Main function to run the Asteroids game.
    Initializes pygame, sets up the game screen, and runs the game loop.
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    dt = 0  # Delta time for frame rate independence
    clock = pygame.time.Clock()

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
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

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

        # Clear screen
        screen.fill("black")

        # Draw game objects
        for object in drawable:
            object.draw(screen)

        pygame.display.flip()  # Update display

        # Control frame rate
        dt = clock.tick(60) / 1000  # Convert ms to seconds

if __name__ == "__main__":
    main()