import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        """
        Initialize the Asteroid object.

        Args:
            x (float): The x-coordinate of the asteroid's initial position.
            y (float): The y-coordinate of the asteroid's initial position.
            radius (float): The radius of the asteroid.
        """
        super().__init__(x, y, radius)
  
    def split(self):
        """
        Split the asteroid into two smaller asteroids if its radius is greater than the minimum radius.
        """
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_rotation = random.uniform(20, 50)
        random_angle1 = self.velocity.rotate(random_rotation)
        random_angle2 = self.velocity.rotate(-random_rotation)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        split_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        split_asteroid1.velocity = random_angle1 * 1.2

        split_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        split_asteroid2.velocity = random_angle2 * 1.2
  
    def draw(self, screen):
        """
        Draw the asteroid on the screen.

        Args:
            screen (pygame.Surface): The surface to draw the asteroid on.
        """
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
  
    def update(self, dt):
        """
        Update the asteroid's position.

        Args:
            dt (float): Delta time for frame rate independence.
        """
        self.position += self.velocity * dt